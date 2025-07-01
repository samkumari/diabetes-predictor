pipeline {
    agent any
    stages {
    stage('Clone Repository') {
        steps {
            echo 'Cloning repository...'
            checkout scm
        }
    }

    stage('Build Docker Image') {
        steps {
            script {
                sh 'docker build -t diabetes-app .'
            }
        }
    }

    stage('Run Docker Container') {
        steps {
            script {
                dockerImage.run('-d -p 5000:5000')
            }
        }
    }
}

post {
    success {
        echo 'Pipeline completed successfully.'
    }
    failure {
        echo 'Pipeline failed. Check the console output.'
    }
}

}
