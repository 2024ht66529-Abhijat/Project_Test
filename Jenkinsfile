pipeline {
    agent any

    stages {
        stage('Setup Python Virtual Env') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t aceest-fitness .'
                sh 'docker run -p 5000:5000 accest-fitness'
            }
        }
    }
}