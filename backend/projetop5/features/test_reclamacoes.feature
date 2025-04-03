Feature: Testar API de Reclamações

  Scenario: Criar uma nova reclamação
    Given que tenho os dados de uma reclamação válida
    When eu envio uma solicitação POST para criar a reclamação
    Then o sistema deve retornar um status 201
