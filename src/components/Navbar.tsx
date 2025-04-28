import React from 'react';
import { Moon, Sun } from 'lucide-react';

const Navbar = () => {
  return (
    <nav className="bg-white dark:bg-gray-900 shadow-sm">
      <div className="container mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="text-xl font-semibold text-gray-800 dark:text-white">
            Logo
          </div>
          <div className="flex items-center space-x-4">
            <button className="text-gray-500 dark:text-gray-400 hover:text-gray-600 dark:hover:text-gray-300">
              <Sun className="h-5 w-5" />
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;