pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t web-app:${BUILD_NUMBER} .'
            }
        }

        stage('Push to Docker Registry') {
            steps {
                sh 'docker push web-app:${BUILD_NUMBER}'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Use kubectl or Kubernetes CLI commands to deploy the application to Kubernetes
                sh 'kubectl apply -f kubernetes-deployment.yaml'
            }
        }
        
        stage('Cleanup') {
            steps {
                sh 'docker rmi web-app:${BUILD_NUMBER}'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }
        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}

