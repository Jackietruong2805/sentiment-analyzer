function App() {
  return (
    <div className="relative h-[100vh] w-[100vw] bg-slate-900 flex items-center justify-center">
      <div className="w-full lg:max-w-[800px] lg:mx-auto -mt-4">
        <div className="px-4 py-2 text-white text-4xl font-semibold text-center">
          <div className="mt-2">Sentiment Analyzer</div>
          <div className="mt-5">
            <textarea
              placeholder="Please enter here..."
              className="min-h-[450px] text-lg p-3 resize-none focus:border-blue-500 border-[3px] transition-all delay-200 shadow-2xl border-gray-400 rounded-md text-gray-900 outline-none lg:max-w-[1000px] lg:w-full max-w-[450px] w-full"
            ></textarea>
            <div className="flex lg:max-w-[1000px] mx-auto lg:w-full max-w-[450px] w-full">
              <div className="flex flex-col gap-3 text-2xl mt-3">
                <button className="whitespace-nowrap px-3 py-1 rounded-md bg-orange-500">
                  Naive Bayes
                </button>
                <button className="whitespace-nowrap px-3 py-1 rounded-md bg-pink-500">
                  Maxent
                </button>
                <button className="whitespace-nowrap px-3 py-1 rounded-md bg-yellow-500">
                  ANN
                </button>
              </div>
              <div className="flex flex-col items-center justify-center w-full">
                <div className="py-2">
                  <span className="text-green-400">Positive</span>
                </div>
                <div className="mt-5">
                  <button className="px-4 py-3 bg-blue-500 text-xl rounded-md">
                    Run Analysis
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
