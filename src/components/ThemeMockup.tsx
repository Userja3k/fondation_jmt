import React from 'react';

const ThemeMockup: React.FC = () => {
  return (
    <div className="flex h-screen w-full">
      {/* Light Mode Background */}
      <div className="flex-1 flex flex-col justify-center items-center bg-jmtgreen-light text-jmtgreen-dark p-8">
        <h2 className="text-4xl font-bold mb-4">Light Mode Background</h2>
        <div className="w-64 h-64 rounded-lg shadow-lg bg-gradient-to-br from-jmtgreen-light to-jmtgreen-accent-light"></div>
        <p className="mt-4 text-lg max-w-xs text-jmtgreen-dark">
          Background color: #f0fdf4 (Light Green)
        </p>
      </div>

      {/* Dark Mode Background */}
      <div className="flex-1 flex flex-col justify-center items-center bg-jmtgreen-dark text-jmtgreen-light p-8">
        <h2 className="text-4xl font-bold mb-4">Dark Mode Background</h2>
        <div className="w-64 h-64 rounded-lg shadow-lg bg-gradient-to-br from-jmtgreen-dark to-jmtgreen-accent-dark"></div>
        <p className="mt-4 text-lg max-w-xs text-jmtgreen-light">
          Background color: #022c22 (Dark Green)
        </p>
      </div>
    </div>
  );
};

export default ThemeMockup;
