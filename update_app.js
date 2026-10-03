const fs = require('fs');

const file = '90_cubefarm_fork_integration/client/src/App.tsx';
let content = fs.readFileSync(file, 'utf8');

const importHook = "import { useEffect } from 'react';\nimport { useStore } from './store';";

content = content.replace("import { StatsReadout", importHook + "\nimport { StatsReadout");

const themeHook = `
export function App() {
  const theme = useStore((s) => s.settings.theme) || 'aurora';

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);
`;

content = content.replace("export function App() {", themeHook);

fs.writeFileSync(file, content);
