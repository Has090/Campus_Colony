export function Intro2() {
  // 1. We define our data as a variable (This will eventually come from your Backend)
  const areaData = {
    location: "Faisal Town Block C",
    stats: [
      { label: "Pharmacies", count: 9, max: 10, icon: "💊" },
      { label: "Food Outlets", count: 17, max: 20, icon: "🍜" },
      { label: "Stationery Shops", count: 6, max: 10, icon: "📚" },
      { label: "ATMs", count: 7, max: 10, icon: "🏧" },
      { label: "Transit Stops", count: 5, max: 10, icon: "🚌" },
    ],
  };

  return (
    <div className="bg-[#1e272e] text-white p-12 flex flex-col md:flex-row items-center justify-between rounded-3xl border-b-8 border-[#ff5e57] shadow-2xl mt-12 gap-12">
      
      {/* LEFT SIDE: Text Information */}
      <div className="max-w-md">
        <div className="text-[#ff5e57] font-bold text-sm tracking-widest uppercase mb-2">Area Intelligence</div>
        <h2 className="text-5xl font-black leading-tight mb-6">
          Know the Area <br /> before <br /> you Rent
        </h2>
        <p className="text-gray-400 leading-relaxed">
          Every rental on <span className="text-white font-bold">CampusColony</span> comes with a full area intelligence report. 
          We scan a 1 km radius using open map data so you know exactly how student-friendly the location is.
        </p>
      </div>

      {/* RIGHT SIDE: The Dynamic Stats Card */}
      <div className="bg-white rounded-2xl p-8 w-full max-w-lg shadow-inner text-gray-800">
        <p className="text-[10px] font-bold text-gray-400 uppercase tracking-[0.2em] mb-8">
          Sample Area Score — {areaData.location}
        </p>

        <div className="space-y-6">
          {/* 2. DYNAMIC MAPPING: This loop draws all 5 bars automatically */}
          {areaData.stats.map((item, index) => (
            <div key={index} className="flex items-center gap-4">
              <span className="text-xl w-6">{item.icon}</span>
              <span className="text-sm font-bold w-32 text-gray-600">{item.label}</span>
              
              {/* The Progress Bar Container */}
              <div className="flex-1 bg-gray-200 h-2 rounded-full overflow-hidden">
                {/* 3. VARIABLE WIDTH: Logic to set bar length based on count */}
                <div 
                  className="bg-[#74452d] h-full rounded-full transition-all duration-1000"
                  style={{ width: `${(item.count / item.max) * 100}%` }}
                ></div>
              </div>
              
              <span className="text-sm font-black w-4 text-right">{item.count}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}