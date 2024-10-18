pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                deleteDir() // Optional: Clear workspace
                git branch: 'main', url: 'https://github.com/germainelry/Simple_Calculator.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Conditional step: Use 'bat' for Windows, 'sh' for Mac/Linux
                script {
                    if (isUnix()) {
                        sh 'pip3 install -r requirements.txt' // Mac/Linux
                    } else {
                        bat 'pip install -r requirements.txt' // Windows
                    }
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Running calculator script...'
                script {
                    if (isUnix()) {
                        sh 'python3 calculator.py 1 10 20' // Mac/Linux
                    } else {
                        bat 'python calculator.py 1 10 20' // Windows
                    }
                }
            }
        }
        stage('Test') {
            steps {
                // Handle test results and platform differences
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    echo 'Running unit tests...'
                    script {
                        if (isUnix()) {
                            sh 'pytest --maxfail=1 --disable-warnings' // Mac/Linux
                        } else {
                            bat 'pytest --maxfail=1 --disable-warnings' // Windows
                        }
                    }
                }
            }
        }
        stage('Deploy to GitHub Pages') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-credentials', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    sh """
                        npm install -g --silent gh-pages@2.1.1
                        git config user.email "germainelry@hotmail.com"
                        git config user.name "germainelry"
                        gh-pages --dotfiles --message '[skip ci] Updates' --dist build
                    """
                }
            }
        }
    }
    post {
        success {
            echo 'Build and test stages completed successfully.'
        }
        failure {
            echo 'One or more stages failed. Check the logs for details.'
        }
    }
}
