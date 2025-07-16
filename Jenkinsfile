pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt || pip install robotframework playwright
                playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . $VENV/bin/activate
                robot --output output.xml --report report.html --log log.html robot/
                '''
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: '*.html, output.xml', fingerprint: true
            }
        }
    }
}
