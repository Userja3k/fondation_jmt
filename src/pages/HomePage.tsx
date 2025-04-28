import React from 'react';

function HomePage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <section className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-6">
          Welcome
        </h1>
        <p className="text-lg text-gray-700 dark:text-gray-300">
          This is the home page of our application.
        </p>
      </section>
    </div>
  );
}

export default HomePage;