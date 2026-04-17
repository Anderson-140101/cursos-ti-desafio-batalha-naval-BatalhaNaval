import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, Alert, Linking, ScrollView } from 'react-native';

export default function App() {
  const agentName = 'Aris';

  // Funções de simulação para integrações nativas
  const handleCalendar = () => {
    Alert.alert(`${agentName}`, 'Acessando calendário... Hoje você não tem compromissos urgentes.');
    // No futuro, isso usaria react-native-calendar-events
  };

  const handleEmail = () => {
    Alert.alert(`${agentName}`, 'Abrindo seu aplicativo de email...');
    Linking.openURL('mailto:');
  };

  const handleDrive = () => {
    Alert.alert(`${agentName}`, 'Redirecionando para o Google Drive...');
    // Exemplo de deeplink, pode requerer configuração adicional no aparelho
    Linking.openURL('googledrive://').catch(() => {
        Alert.alert('Erro', 'Google Drive não está instalado.');
    });
  };

  const handleScan = () => {
    Alert.alert(`${agentName}`, 'Iniciando câmera para escanear documento e salvar no Drive...');
    // No futuro, usaria expo-camera e api do google drive
  };

  const handleCall = () => {
    Alert.alert(`${agentName}`, 'Iniciando chamada...');
    Linking.openURL('tel:123456789'); // Exemplo de deeplink para telefone
  };

  const handleListen = () => {
    Alert.alert(`${agentName}`, 'Escutando... (Simulando reconhecimento de voz "Ok Aris")');
    // No futuro, usaria @react-native-voice/voice ou similar para detecção contínua
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🤖 Olá, eu sou {agentName}!</Text>
      <Text style={styles.subtitle}>Seu assistente pessoal para celular.</Text>

      <View style={styles.buttonContainer}>
        <Button title="Simular Wake Word (Falar 'Aris')" onPress={handleListen} color="#4CAF50" />
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
    paddingTop: 80,
    paddingHorizontal: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginBottom: 40,
    textAlign: 'center',
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: '600',
    marginTop: 30,
    marginBottom: 20,
  },
  buttonContainer: {
    width: '100%',
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
