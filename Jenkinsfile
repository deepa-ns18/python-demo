pipeline {
    agent {
      label 'linux-agent'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                python3.11 --version
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                python3.11 app.py
                '''
            }
        }
    }
}
