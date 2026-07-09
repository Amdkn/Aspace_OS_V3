import React from 'react';
import { SectionTitle } from '../atoms/SectionTitle';
import { ServiceCard } from '../molecules/ServiceCard';

const services = [
  {
    title: "Ingénierie de Process",
    description: "Conception et optimisation de lignes de production industrielle avec une approche axée sur l'efficacité.",
    iconName: "Zap" as const
  },
  {
    title: "Maintenance Prédictive",
    description: "Utilisation de l'IA pour anticiper les pannes et réduire les temps d'arrêt de vos équipements.",
    iconName: "Activity" as const
  },
  {
    title: "Conseil Technique",
    description: "Accompagnement stratégique dans le choix de technologies et la transformation numérique industrielle.",
    iconName: "Shield" as const
  },
  {
    title: "Solutions Automatisation",
    description: "Intégration de robots et de systèmes automatisés pour booster votre productivité globale.",
    iconName: "Bot" as const
  },
  {
    title: "Audit Énergétique",
    description: "Analyse complète de votre consommation énergétique pour des économies durables et responsables.",
    iconName: "Zap" as const
  },
  {
    title: "Formation Technique",
    description: "Programmes de formation sur mesure pour vos équipes opérationnelles et de maintenance.",
    iconName: "Book" as const
  }
];

export const ServicesGrid: React.FC = () => {
  return (
    <section className="py-24 px-6 max-w-7xl mx-auto">
      <SectionTitle 
        title="Nos Services Expertise" 
        subtitle="Des solutions d'ingénierie complètes pour répondre aux défis industriels de demain."
        centered
      />
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {services.map((service, index) => (
          <ServiceCard 
            key={index}
            title={service.title}
            description={service.description}
            iconName={service.iconName}
          />
        ))}
      </div>
    </section>
  );
};
