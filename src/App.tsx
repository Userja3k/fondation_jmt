import React, { useState, useEffect } from 'react';
import { Moon, Sun } from 'lucide-react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import { ThemeProvider } from './context/ThemeContext';

function App() {
  return (
    <ThemeProvider>
      <div className="font-sans">
        <Navbar />
        <main>
          <HomePage />
        </main>
        <Footer />
      </div>
    </ThemeProvider>
  );
}

export default App;