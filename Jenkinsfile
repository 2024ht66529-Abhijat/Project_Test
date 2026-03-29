pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<2024ht66529-Abhijat>/Project_Test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t aceest-fitness:latest .'
            }
        }
    }
}