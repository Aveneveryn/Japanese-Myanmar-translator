document.getElementById('txtForm').addEventListener('submit', async function(e){
  e.preventDefault();
  const text = document.getElementById('text').value;
  const resDiv = document.getElementById('result');
  resDiv.textContent = 'Translating...';
  const resp = await fetch('/api/translate/text', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({text})
  });
  const data = await resp.json();
  if(resp.ok){
    resDiv.innerHTML = '<pre>'+JSON.stringify(data,null,2)+'</pre>' +
      '<button id="speak">Play JP</button>';
    document.getElementById('speak').addEventListener('click', function(){
      const utter = new SpeechSynthesisUtterance(data.jp);
      utter.lang = 'ja-JP';
      speechSynthesis.speak(utter);
    });
  } else {
    resDiv.textContent = JSON.stringify(data);
  }
});
