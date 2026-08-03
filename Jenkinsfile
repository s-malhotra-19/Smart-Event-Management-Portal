pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/S-Malhotra-19/Smart-Event-Management-Portal.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t saksham2262/eventportal:v3 .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images'
            }
        }

    }
}