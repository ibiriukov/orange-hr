pipeline {
  agent any
  stages {
    stage('Checkout'){ steps { checkout scm } }
    stage('Setup'){
      steps {
        bat '''
          py -3 -m venv .venv
          call .venv\\Scripts\\activate
          pip install --upgrade pip
          pip install -r requirements.txt
          py -3 -m playwright install
        '''
      }
    }
    stage('Test'){
      steps {
        withCredentials([
          usernamePassword(credentialsId: 'orangehrm-creds',
                           usernameVariable: 'ORANGE_USERNAME',
                           passwordVariable: 'ORANGE_PASSWORD'),
          string(credentialsId: 'orangehrm-base-url',
                 variable: 'ORANGE_BASE_URL')
        ]) {
          bat '''
            call .venv\\Scripts\\activate
            pytest -v --junitxml=test-results\\junit.xml ^
                   --html=report.html --self-contained-html
          '''
        }
      }
    }
  }
  post {
    always {
      junit 'test-results/junit.xml'
      archiveArtifacts artifacts: 'report.html,test-results/**', fingerprint: true
    }
  }
}
