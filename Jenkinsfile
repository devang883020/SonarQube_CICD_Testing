pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv('sonarqube') {
          sh '''
            sonar-scanner \
            -Dsonar.projectKey=myapp \
            -Dsonar.sources=. \
            -Dsonar.login=$SONAR_TOKEN
          '''
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
  }
}
