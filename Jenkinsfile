pipeline {
    agent any

    environment {
        SONARQUBE_ENV = 'sonarqube'
        DOCKER_IMAGE  = 'devangkubde88/my-docker-app'
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Install Test Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install pytest pytest-cov
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh '''
                . venv/bin/activate
		export PYTHONPATH=$(pwd)
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
                ${scannerHome}/bin/sonar-scanner
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
                docker build -t $DOCKER_IMAGE:latest .
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
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker push $DOCKER_IMAGE:latest
            '''
        }
    }
}

}
    post {
        success {
            echo "✅ Pipeline successful — Quality gate passed & image pushed"
        }
        failure {
            echo "❌ Pipeline failed — fix errors before proceeding"
        }
    }
}
