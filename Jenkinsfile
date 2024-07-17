pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my_flask_app"
    }

    stages {
        stage('Pull Source Code') {
            steps {
                git 'https://github.com/AishGoyal/my_flask_app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("${env.DOCKER_IMAGE}").inside {
                        sh 'pytest --junitxml=test-results.xml'
                    }
                }
            }
        }

        stage('Report Test Results') {
            steps {
                junit 'test-results.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'test-results.xml', allowEmptyArchive: true
            cleanWs()
        }
    }
}
