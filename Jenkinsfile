pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jonathan-pp/devops-158-Pinto2-tp.git'
            }
        }
        stage('Pull latest code') {
            steps {
                dir('/home/pi_158_pinto2/devops-158-Pinto2-tp/') {
                    git branch: 'main', url: 'https://github.com/jonathan-pp/devops-158-Pinto2-tp.git'
                }
            }
        }
        stage('Install dependencies') {
            steps {
                dir('/home/pi_158_pinto2/devops-158-Pinto2-tp/') {
                    sh '''#!/bin/bash
                        source venv/bin/activate
                        pip install flask
                    '''
                }
            }
        }
        stage('Restart Flask app') {
            steps {
                script {
                    sh 'sudo pkill -f "python app.py" || true'
                    sh 'sudo systemctl restart flask-app'
                }
            }
        }
    }
    post {
        success {
            echo 'Déploiement automatique réussi ! BRAVO DAMN'
        }
        failure {
            echo 'Échec du pipeline. - AIE AIE AIE CA PUE'
        }
    }
}
