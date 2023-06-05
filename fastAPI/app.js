async function fetchData() {
    try {
      const response = await fetch('http://127.0.0.1:8000/'); // Substitua o endereço pelo seu endpoint local
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.log('Ocorreu um erro:', error);
    }
  }
fetchData();
