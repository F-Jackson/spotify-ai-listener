import React from 'react';
import ReactDOM from 'react-dom/client';
import Router from 'routes';
import './index.css';
import { CookiesProvider } from "react-cookie";

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <CookiesProvider>
    <React.StrictMode>
      <Router />
    </React.StrictMode>
  </CookiesProvider>
);
