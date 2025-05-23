import React, { useEffect, useState } from 'react';
import axios from 'axios';

// El componente principal de la aplicación
function App() {
  // Estado para almacenar el mensaje recibido del backend
  const [message, setMessage] = useState('');
  // Estado para manejar el estado de carga de la petición
  const [loading, setLoading] = useState(true);
  // Estado para manejar cualquier error que ocurra durante la petición
  const [error, setError] = useState(null);

  // useEffect se ejecuta una vez después del renderizado inicial del componente
  // Es ideal para realizar peticiones de datos
  useEffect(() => {
    // Configura el estado de carga a true al inicio de la petición
    setLoading(true);
    // Realiza una petición GET al endpoint de tu backend
    // Asegúrate de que tu servidor Django esté corriendo en http://127.0.0.1:8000
    // y que CORS esté correctamente configurado para permitir peticiones desde tu aplicación React.
    axios.get('http://127.0.0.1:8000/api/hello/')
      .then(response => {
        // Si la petición es exitosa, actualiza el estado 'message' con los datos recibidos
        setMessage(response.data.message);
        // Limpia cualquier error previo
        setError(null);
      })
      .catch(err => {
        // Si ocurre un error, imprímelo en la consola
        console.error('Hubo un error al conectar con el backend:', err);
        // Actualiza el estado 'error' con un mensaje descriptivo
        setError('Error al conectar con el backend. Por favor, asegúrate de que el servidor esté corriendo y CORS esté configurado.');
        // Establece el mensaje a vacío si hay un error
        setMessage('');
      })
      .finally(() => {
        // Independientemente de si la petición fue exitosa o falló,
        // establece el estado de carga a false
        setLoading(false);
      });
  }, []); // El array vacío de dependencias asegura que este efecto se ejecute solo una vez al montar el componente

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4 font-sans">
      <div className="bg-white p-8 rounded-lg shadow-xl text-center max-w-md w-full">
        <h1 className="text-3xl font-bold text-gray-800 mb-6">
          Comunicación con Backend
        </h1>
        <div className="p-4 bg-blue-50 border border-blue-200 rounded-md">
          {loading && (
            <p className="text-blue-600 text-lg">Cargando mensaje del backend...</p>
          )}
          {error && (
            <p className="text-red-600 text-lg font-medium">{error}</p>
          )}
          {!loading && !error && (
            <p className="text-gray-700 text-lg">
              <span className="font-semibold">Mensaje del Backend:</span> {message}
            </p>
          )}
        </div>
        <p className="mt-6 text-sm text-gray-500">
          Asegúrate de que tu servidor Django esté funcionando en `http://127.0.0.1:8000` y que CORS esté configurado.
        </p>
      </div>
    </div>
  );
}

export default App;
