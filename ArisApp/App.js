import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, Alert, Linking, ScrollView, TextInput, ActivityIndicator } from 'react-native';
import { useState } from 'react';
import { GoogleGenerativeAI } from '@google/generative-ai';

// ATENÇÃO: Substitua 'SUA_CHAVE_API_AQUI' pela sua chave de API real do Google Gemini.
// Em um aplicativo real em produção, NUNCA deixe a chave da API exposta no código.
const GEMINI_API_KEY = 'SUA_CHAVE_API_AQUI';

export default function App() {
  const agentName = 'Aris';

  const [prompt, setPrompt] = useState('');
  const [resposta, setResposta] = useState('Me pergunte qualquer coisa!');
  const [carregando, setCarregando] = useState(false);

  // Função para falar com o Gemini
  const falarComAris = async () => {
    if (!prompt.trim()) return;

    if (GEMINI_API_KEY === 'SUA_CHAVE_API_AQUI') {
        Alert.alert("Chave API Faltando", "Você precisa colocar a sua chave de API do Gemini no código (App.js) para a inteligência artificial funcionar.");
        return;
    }

    setCarregando(true);
    setResposta('Pensando...');

    try {
      const genAI = new GoogleGenerativeAI(GEMINI_API_KEY);
      // Usando o modelo gemini-1.5-pro conforme solicitado pelo usuário
      const model = genAI.getGenerativeModel({ model: "gemini-1.5-pro" });

      const instrucaoSistema = `Você é um assistente virtual pessoal chamado ${agentName}. Você é prestativo, educado e fala português. Responda de forma concisa como um assistente de celular.`;

      const result = await model.generateContent(`${instrucaoSistema}\n\nUsuário: ${prompt}`);
      const response = await result.response;
      const texto = response.text();

      setResposta(texto);
    } catch (error) {
      console.error(error);
      setResposta('Desculpe, ocorreu um erro ao me conectar com meu cérebro (Gemini).');
    } finally {
      setCarregando(false);
      setPrompt('');
    }
  };

  // Funções de simulação para integrações nativas
  const handleCalendar = () => {
    Alert.alert(`${agentName}`, 'Acessando calendário... Hoje você não tem compromissos urgentes.');
  };

  const handleEmail = () => {
    Alert.alert(`${agentName}`, 'Abrindo seu aplicativo de email...');
    Linking.openURL('mailto:');
  };

  const handleDrive = () => {
    Alert.alert(`${agentName}`, 'Redirecionando para o Google Drive...');
    Linking.openURL('googledrive://').catch(() => {
        Alert.alert('Erro', 'Google Drive não está instalado.');
    });
  };

  const handleScan = () => {
    Alert.alert(`${agentName}`, 'Iniciando câmera para escanear documento e salvar no Drive...');
  };

  const handleCall = () => {
    Alert.alert(`${agentName}`, 'Iniciando chamada...');
    Linking.openURL('tel:123456789');
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🤖 Olá, eu sou o {agentName}!</Text>

      {/* Área do Chat com o Gemini */}
      <View style={styles.chatContainer}>
        <Text style={styles.respostaAris}>{resposta}</Text>

        {carregando && <ActivityIndicator size="large" color="#0000ff" style={{marginVertical: 10}} />}

        <TextInput
          style={styles.input}
          placeholder="Fale com o Aris..."
          value={prompt}
          onChangeText={setPrompt}
          multiline
        />
        <Button
            title="Enviar mensagem"
            onPress={falarComAris}
            color="#2196F3"
            disabled={carregando}
        />
      </View>

      <Text style={styles.sectionTitle}>Comandos Simulados:</Text>

      <View style={styles.grid}>
        <View style={styles.buttonWrapper}>
          <Button title="📅 Ver Calendário" onPress={handleCalendar} />
        </View>
        <View style={styles.buttonWrapper}>
          <Button title="✉️ Ver Emails" onPress={handleEmail} />
        </View>
        <View style={styles.buttonWrapper}>
          <Button title="☁️ Abrir Drive" onPress={handleDrive} />
        </View>
        <View style={styles.buttonWrapper}>
          <Button title="📸 Escanear Documento" onPress={handleScan} />
        </View>
        <View style={styles.buttonWrapper}>
          <Button title="📞 Fazer Ligação" onPress={handleCall} />
        </View>
      </View>

      <StatusBar style="auto" />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    paddingTop: 60,
    paddingHorizontal: 20,
    paddingBottom: 40
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  chatContainer: {
    width: '100%',
    backgroundColor: '#f5f5f5',
    padding: 15,
    borderRadius: 10,
    marginBottom: 30,
    minHeight: 200,
  },
  respostaAris: {
    fontSize: 16,
    color: '#333',
    marginBottom: 20,
    fontStyle: 'italic',
  },
  input: {
    backgroundColor: '#fff',
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    padding: 10,
    marginBottom: 10,
    minHeight: 50,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: '600',
    marginBottom: 20,
  },
  grid: {
    width: '100%',
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  buttonWrapper: {
    width: '48%',
    marginBottom: 15,
  }
});
