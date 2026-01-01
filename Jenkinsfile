pipeline {
    agent any

    environment {
        IMAGE_NAME = "devangkubde88/my-docker-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        GITOPS_REPO = "https://github.com/devang883020/SonarQube_CICD_Testing.git"
SONARQUBE_ENV = 'sonarqube'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pytest --cov=app --cov-report=xml
                '''
            }
        }


        stage('SonarQube Analysis') {
    steps {
        withSonarQubeEnv('sonarqube') {
            script {
                def scannerHome = tool 'sonar-scanner'
                sh """
                ${scannerHome}/bin/sonar-scanner \
                -Dsonar.projectKey=myapp \
                -Dsonar.sources=app \
                -Dsonar.tests=tests \
                -Dsonar.python.coverage.reportPaths=coverage.xml
                """
            }
        }
    }
}
   
 
        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:latest
                '''
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-cred',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE_NAME:$IMAGE_TAG
                    docker push $IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Update Helm Values (GitOps)') {
            steps {
                sh '''
                rm -rf gitops
                git clone $GITOPS_REPO gitops
                cd gitops

                sed -i "s/tag:.*/tag: ${IMAGE_TAG}/" gitops-myapp/myapp/values.yaml

                git config user.email "jenkins@ci.com"
                git config user.name "Jenkins CI"
                git add gitops-myapp/myapp/values.yaml
                git commit -m "Update image tag to ${IMAGE_TAG}"
                git push origin main
                '''
            }
        }
    }

    post {
        failure {
            echo "❌ Pipeline failed — fix errors before proceeding"
        }
        success {
            echo "✅ Image deployed via GitOps + ArgoCD"
        }
    }
}
