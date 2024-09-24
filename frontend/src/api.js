const API_BASE_URL = '/api';

export const analyzePrompt = async (prompt, model, goal) => {
  const response = await fetch(`${API_BASE_URL}/analyze-prompt`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ prompt, model, goal }),
  });

  if (!response.ok) {
    throw new Error('Failed to analyze prompt');
  }

  return response.json();
};

export const generateTest = async (prompt, model, goal) => {
    const response = await fetch(`${API_BASE_URL}/generate-test`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt, model, goal }),
    });
  
    if (!response.ok) {
      throw new Error('Failed to generate test');
    }
  
    return response.json();
  };
  
  export const executePrompt = async (prompt, model) => {
    const response = await fetch(`${API_BASE_URL}/execute-prompt`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt, model }),
    });
  
    if (!response.ok) {
      throw new Error('Failed to execute prompt');
    }
  
    return response.text();
  };