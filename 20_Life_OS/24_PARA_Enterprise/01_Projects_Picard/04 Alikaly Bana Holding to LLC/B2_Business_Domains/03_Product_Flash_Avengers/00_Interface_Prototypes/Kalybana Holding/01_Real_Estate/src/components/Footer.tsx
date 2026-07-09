export default function Footer() {
  return (
    <footer className="bg-surface border-t border-on-surface/10 py-16">
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-12">
          <div className="space-y-4">
            <div className="font-bold text-on-surface text-lg font-headline">Ali Real Estate Bana LLC</div>
            <p className="font-label text-sm text-secondary leading-relaxed max-w-sm">
              © 2024 Ali Real Estate Bana LLC. Asset Recovery Specialists in Ohio & Kentucky. Specialized in surplus fund recovery and judicial sale auditing.
            </p>
          </div>
          <nav className="flex flex-wrap gap-x-8 gap-y-4">
            <a className="font-label text-sm text-secondary hover:text-primary transition-colors" href="#">Privacy Policy</a>
            <a className="font-label text-sm text-secondary hover:text-primary transition-colors" href="#">Terms of Service</a>
            <a className="font-label text-sm text-secondary hover:text-primary transition-colors" href="#">Contact Us</a>
            <a className="font-label text-sm text-secondary hover:text-primary transition-colors" href="#">Affiliations</a>
          </nav>
        </div>
        <div className="mt-16 pt-8 border-t border-on-surface/5 flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="flex items-center gap-6 opacity-40 grayscale">
            <img
              alt="Legal Shield Logo"
              className="h-8"
              src="https://lh3.googleusercontent.com/aida-public/AB6AXuB-BhN4zuMXj2CMXxcnZQ7-nw-9_BJ0bxzvPeT9r5bhT9iDoBtnUG9m7P6JIVJps7YXJVkRwYpe9IukY0t0b5phwi6ugNGGLme1LXVKe9JMPty3ytiSzxUCvIRLS7ik48f1VS5I8AUz0b-qt1Uc4j6UGzM69GZ7PNljQd1fK8xoS59f9XP9KCBsMRTsMNURrF3wknS52WJxsFidtAiyLIBpMUUNqrBk-TL9rv1X1G8Kmw-f3EpcoyIoK917q7ygIn0qYJOJhfcEVEo"
            />
            <img
              alt="Fair Housing Logo"
              className="h-8"
              src="https://lh3.googleusercontent.com/aida-public/AB6AXuCWt6RZ5zPSd4d6nlYCiGfcgcx7C2IPVAa1BXzrND0JPAUUd3dUoZX1wFPU3AsnrpbzMiHTFShDt5_O32vKG967vmoD9PG32J34QDqqydAszD4OSAe0iPz3bcCaFYECz0PYbs3IUNbL6sME853gTs2BdMJDlQmlGsNtdltVFAzzZGcpsnTizI60AO6q7SAkmtap98RatxtSH2-_QqrDjLrkk0CSojbwIZuFH2UFAo08nxBLLP2glflWutm9dnAHMvz7H41vob_uwcc"
            />
          </div>
          <div className="text-xs font-label text-secondary/40">
            NMLS: #RE-44092-OH | Firm ID: KY-992031
          </div>
        </div>
      </div>
    </footer>
  );
}
