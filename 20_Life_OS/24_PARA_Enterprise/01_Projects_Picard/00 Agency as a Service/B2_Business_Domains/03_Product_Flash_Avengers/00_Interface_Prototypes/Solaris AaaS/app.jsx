/* global React, ReactDOM, window */
// SOLARIS — root app

const { useEffect } = React;

const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "icp": "aaa",
  "density": "comfortable"
}/*EDITMODE-END*/;

function App() {
  const [tweaks, setTweak] = window.useTweaks(TWEAK_DEFAULTS);

  // mirror archetype/density into the document for CSS theming
  useEffect(() => {
    document.documentElement.setAttribute("data-archetype", tweaks.icp);
    document.documentElement.setAttribute("data-density", tweaks.density);
  }, [tweaks.icp, tweaks.density]);

  const setIcp = (id) => setTweak("icp", id);

  return (
    <div className="page">
      <Topbar icp={tweaks.icp} setIcp={setIcp} />
      <Hero icp={tweaks.icp} />
      <HookSection />
      <AnatomySection />
      <MarginShieldSection />
      <WheelSection />
      <ArchetypeSection icp={tweaks.icp} setIcp={setIcp} />
      <ParadigmSection />
      <VaultSection icp={tweaks.icp} />
      <FinalCTA />
      <Footer />

      <window.TweaksPanel>
        <window.TweakSection label="Archétype-cible actif">
          <window.TweakRadio
            label="Wave 01"
            value={tweaks.icp}
            options={[
              { value: "revops", label: "RevOps" },
              { value: "forges", label: "Forges" },
              { value: "aaa", label: "AAA" },
              { value: "boutiques", label: "Boutiques" },
            ]}
            onChange={(v) => setTweak("icp", v)}
          />
        </window.TweakSection>
        <window.TweakSection label="Densité">
          <window.TweakRadio
            label="Spacing"
            value={tweaks.density}
            options={[
              { value: "compact", label: "Compact" },
              { value: "comfortable", label: "Confort" },
              { value: "spacious", label: "Aéré" },
            ]}
            onChange={(v) => setTweak("density", v)}
          />
        </window.TweakSection>
      </window.TweaksPanel>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
