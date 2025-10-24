// Schema.org Structured Data para Mana Money Exchange
const schemaData = {
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Mana Money Exchange",
  "image": "img/mana_logowhite.png",
  "description": "Casa de cambio en Cartagena con las mejores tasas de divisas. Más de 20 años de experiencia.",
  "url": "https://manamoneyexchange.com",
  "telephone": "+573016226750",
  "email": "info@manamoneyexchange.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle 34 Portocarrero #06-6",
    "addressLocality": "Cartagena de Indias",
    "addressRegion": "Bolívar",
    "addressCountry": "CO"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "10.423410789661766",
    "longitude": "-75.55213788907803"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
      "opens": "09:00",
      "closes": "17:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Sunday",
      "opens": "08:00",
      "closes": "14:00"
    }
  ],
  "priceRange": "$$",
  "currenciesAccepted": "USD, EUR, GBP, MXN, ARS, BRL, COP",
  "paymentAccepted": "Cash"
};

// Insertar el schema en el head del documento
const script = document.createElement('script');
script.type = 'application/ld+json';
script.text = JSON.stringify(schemaData);
document.head.appendChild(script);
