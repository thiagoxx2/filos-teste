<?php
/**
 * send_ouvidoria.php - Envio seguro de relatos da Ouvidoria com validação do Google reCAPTCHA v2
 * Faculdade Filos
 */

header('Content-Type: application/json; charset=utf-8');

// --- CONFIGURAÇÕES ---
// Substitua estas chaves pelas suas chaves oficiais do Google reCAPTCHA v2 obtidas no console do Google
define('RECAPTCHA_SECRET_KEY', '6LeIxAcTAAAAAGG-vFI1TnFTxWqCD1Sp29saZmWw'); // CHAVE SECRETA DE TESTES GLOBAIS DO GOOGLE
define('DESTINATARIO_EMAIL', 'ouvidoria@faculdadefilos.com.br');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Método não permitido.']);
    exit;
}

// 1. Receber e sanitizar dados do formulário
$nome = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_SPECIAL_CHARS);
$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
$assunto = filter_input(INPUT_POST, 'assunto', FILTER_SANITIZE_SPECIAL_CHARS);
$mensagem = filter_input(INPUT_POST, 'mensagem', FILTER_SANITIZE_SPECIAL_CHARS);
$recaptcha_response = filter_input(INPUT_POST, 'g-recaptcha-response', FILTER_DEFAULT);

// Validar preenchimento dos campos obrigatórios
if (empty($nome) || !$email || empty($assunto) || empty($mensagem)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Por favor, preencha todos os campos obrigatórios com dados válidos.']);
    exit;
}

// 2. Validar o reCAPTCHA com a API do Google
if (empty($recaptcha_response)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Por favor, marque a caixa de verificação "Não sou um robô".']);
    exit;
}

$verify_url = 'https://www.google.com/recaptcha/api/siteverify';
$data = [
    'secret' => RECAPTCHA_SECRET_KEY,
    'response' => $recaptcha_response,
    'remoteip' => $_SERVER['REMOTE_ADDR']
];

$options = [
    'http' => [
        'header' => "Content-type: application/x-www-form-urlencoded\r\n",
        'method' => 'POST',
        'content' => http_build_query($data)
    ]
];

$context = stream_context_create($options);
$response = file_get_contents($verify_url, false, $context);
$response_keys = json_decode($response, true);

if (!$response_keys['success']) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Falha na verificação de segurança do reCAPTCHA. Tente novamente.']);
    exit;
}

// 3. Montar e enviar o e-mail
$email_subject = "Ouvidoria Filos - Novo Relato: " . htmlspecialchars_decode($assunto, ENT_QUOTES);

// Corpo do e-mail em formato HTML limpo e profissional
$email_body = "
<html>
<head>
  <title>Novo relato enviado via Ouvidoria</title>
</head>
<body style='font-family: Arial, sans-serif; line-height: 1.6; color: #333;'>
  <div style='max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px;'>
    <h2 style='color: #07162c; border-bottom: 2px solid #07162c; padding-bottom: 10px;'>Faculdade Filos - Canal de Ouvidoria</h2>
    <p><strong>Nome:</strong> " . htmlspecialchars($nome) . "</p>
    <p><strong>E-mail de Contato:</strong> " . htmlspecialchars($email) . "</p>
    <p><strong>Assunto do Relato:</strong> " . htmlspecialchars($assunto) . "</p>
    <div style='background-color: #f9f9f9; padding: 15px; border-left: 4px solid #07162c; margin-top: 15px; border-radius: 4px;'>
      <p style='margin: 0; font-weight: bold;'>Mensagem/Relato:</p>
      <p style='white-space: pre-wrap; margin-top: 10px;'>" . nl2br(htmlspecialchars($mensagem)) . "</p>
    </div>
    <p style='font-size: 11px; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px;'>Este relato foi submetido com segurança a partir da página oficial da Ouvidoria da Faculdade Filos.</p>
  </div>
</body>
</html>
";

// Configurar cabeçalhos para evitar cair na caixa de spam (HostGator friendly)
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8" . "\r\n";
$headers .= "From: Ouvidoria Faculdade Filos <no-reply@faculdadefilos.com.br>" . "\r\n";
$headers .= "Reply-To: " . $email . "\r\n";
$headers .= "X-Mailer: PHP/" . phpversion();

// Disparar o e-mail
if (mail(DESTINATARIO_EMAIL, $email_subject, $email_body, $headers)) {
    echo json_encode(['success' => true, 'message' => 'Seu relato foi enviado com sucesso sob total sigilo. Entraremos em contato se necessário.']);
} else {
    http_response_code(500);
    echo json_encode(['success' => false, 'message' => 'Desculpe, ocorreu um erro interno no servidor ao tentar enviar seu e-mail. Por favor, tente novamente mais tarde ou envie diretamente para o e-mail da ouvidoria.']);
}
