pipeline {
  agent any

  environment {
    IMAGE_NAME = "dockerhub_username/devops-day2"
    IMAGE_TAG  = "${BUILD_NUMBER}"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('SonarQube Analysis') {
      steps {
        script {
          def scannerHome = tool 'sonar-scanner'
          withSonarQubeEnv('sonarqube') {
            sh """
              ${scannerHome}/bin/sonar-scanner \
              -Dsonar.projectKey=myapp \
              -Dsonar.sources=.
            """
          }
        }
      }
    }

    stage('Quality Gate') {
      steps {
        timeout(time: 2, unit: 'MINUTES') {
          waitForQualityGate abortPipeline: true
        }
      }
    }

    stage('Docker Build') {
      steps {
        sh """
          docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
        """
      }
    }

    stage('Docker Push') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-cred',
          usernameVariable: 'DOCKER_USER',
          passwordVariable: 'DOCKER_PASS'
        )]) {
          sh """
            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
            docker push ${IMAGE_NAME}:${IMAGE_TAG}
          """
        }
      }
    }
  }
}
