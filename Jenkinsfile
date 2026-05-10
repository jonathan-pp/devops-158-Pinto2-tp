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
                sh '''
<<<<<<< HEAD
=======
                    git config --global --add safe.directory /home/pi_158_pinto2/devops-158-Pinto2-tp

>>>>>>> 80b25e3 (test)
                    if [ -d "/home/pi_158_pinto2/devops-158-Pinto2-tp/.git" ]; then
                        cd /home/pi_158_pinto2/devops-158-Pinto2-tp/
                        git pull origin main
                    else
                        git clone https://github.com/jonathan-pp/devops-158-Pinto2-tp.git \
                            /home/pi_158_pinto2/devops-158-Pinto2-tp/
                    fi
                '''
            }
        }
        stage('Install dependencies') {
            steps {
                dir('/home/pi_158_pinto2/devops-158-Pinto2-tp/') {
                    sh '''
                        source venv/bin/activate
                        pip install flask
                    '''
                }
            }
        }
        stage('Restart Flask app') {
            steps {
                sh '''
                    pkill -f "python app.py" || true
                    cd /home/pi_158_pinto2/devops-158-Pinto2-tp/
                    source venv/bin/activate
                    nohup python app.py > flask.log 2>&1 &
                '''
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