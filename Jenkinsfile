pipeline {
    agent {
        label 'weops-lite'
    }

    environment {
        NOTIFICATION_URL = credentials('NOTIFICATION_URL')
    }

    stages {
        stage('下载代码') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/WeOps-Lab/weops_lite.git'
            }
        }

        stage('编译Web') {   
            steps {
                dir('web') {
                    sh '''
                        sudo n 14.16.0
                        npm i
                        npm run build
                    '''
                }
            }
        }

        stage('拷贝Web资源'){
            steps {
                dir('.'){
                    sh '''
                        mkdir -p ./assets/static
                        cp -Rf ./web/static/dist ./assets/static
                        cp -Rf ./web/static/dist ./static/
                        cp -Rf ./web/static/dist/index.prod.html ./templates/
                    '''
                }
            }
        }

        stage('构建镜像') {
            steps {
                dir('.'){
                    sh '''
                        sudo docker build -f ./support-files/docker/Dockerfile -t ccr.ccs.tencentyun.com/megalab/weops-lite .
                    '''
                }
            }
        }
    }

    post {
        success {
            sh '''
                curl -X POST $NOTIFICATION_URL \
                -H 'Content-Type: application/json' \
                -d '{
                    "content": "WeOps Lite 构建成功"
                }'
            '''
        }
        failure {
            sh '''
                curl -X POST $NOTIFICATION_URL \
                -H 'Content-Type: application/json' \
                -d '{
                    "content": "WeOps Lite 构建失败"
                }'
            '''
        }
    }
}