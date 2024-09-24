import React, { useState, useEffect } from 'react';
import CodeEditor from './components/CodeEditor';
import ModelSelector from './components/ModelSelector';
import ConsoleLog from './components/ConsoleLog';
import GoalInput from './components/GoalInput';
import TestPanel from './components/TestPanel';
import Output from './components/Output';
import Analysis from './components/Analysis';
import { analyzePrompt, generateTest, executePrompt } from './api';

const App = () => {
  const [prompt, setPrompt] = useState('');
  const [goal, setGoal] = useState('');
  const [model, setModel] = useState('claude-3-opus-20240229');
  const [analysis, setAnalysis] = useState(null);
  const [logs, setLogs] = useState([]);
  const [tests, setTests] = useState([]);
  const [output, setOutput] = useState('');

  useEffect(() => {
    const debounce = setTimeout(() => {
      if (prompt) {
        analyzePrompt(prompt, model, goal)
          .then(setAnalysis)
          .catch(error => setLogs(prev => [...prev, { type: 'error', message: error.message }]));
      }
    }, 1000);

    return () => clearTimeout(debounce);
  }, [prompt, model, goal]);

  const handleGenerateTest = async () => {
    try {
      const newTest = await generateTest(prompt, model, goal);
      setTests(prev => [...prev, newTest]);
    } catch (error) {
      setLogs(prev => [...prev, { type: 'error', message: error.message }]);
    }
  };

  const handleExecute = async () => {
    try {
      const result = await executePrompt(prompt, model);
      setOutput(result);
    } catch (error) {
      setLogs(prev => [...prev, { type: 'error', message: error.message }]);
    }
  };

  return (
    <div className="container mx-auto p-4 bg-base-200 min-h-screen">
      <h1 className="text-2xl font-bold mb-4">Prompt Engineering Tool</h1>
      <div className="grid grid-cols-1 gap-4">
        <ModelSelector model={model} setModel={setModel} />
        <GoalInput value={goal} onChange={setGoal} />
        <CodeEditor value={prompt} onChange={setPrompt} analysis={analysis} />
        <div className="flex space-x-2">
          <button className="btn btn-primary" onClick={handleGenerateTest}>Generate Test</button>
          <button className="btn btn-secondary" onClick={handleExecute}>Execute</button>
        </div>
        <Analysis analysis={analysis} />
        <TestPanel tests={tests} />
        <Output content={output} />
        <ConsoleLog logs={logs} />
      </div>
    </div>
  );
};

export default App;