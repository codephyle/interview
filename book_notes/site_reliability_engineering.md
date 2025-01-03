# SRE

    Operations as Software problem
    Without SLOs, there is no SRE

    Feature velocity vs. Reliability

    Blameless postmordems

# Devops 
  
    Constant feedback dev <-> ops
    Individual knowledge, which is then turned into team and organizational knowledge

# SLI - Service Level Indicators
    - latency [also throughput, goodput, error rate etc.,]
    - availability
    - durability

# SLO 

    * Error-budget per quarter. every app gets an error budget. 
    * As long as, SLO remains within error budget, new releases allowed.

        99.9   -> 8 hours / per year
        99.99  -> 50 mins
        99.999 -> 5 mins

    Interestingly, sometimes the SLO are merely met, not significantly exceed to
    make sure the dependents are designed for expected SLO.

    ------------------------------------
    | bang-bang control.                |
    |                                   |
    | on-off systems. like water heater |
    -------------------------------------

# SLA 

    SLA is businesss level agreement.

# Eliminate toil 

    Toil - Repetitive, automatable, manual, answering pagers etc.,


Monitoring - Collecting, aggregating and displaying quantitative insights of a system

# Golden Signals 
    
    - Latency
        - Success latency versus Failure latency
        - High failure latency more dangerous

    - Error rate 
    - Traffic
    - Saturation

# Things

    SRE == Measure, Analyse, Decide, Act, Reflect and Repeat / Share
    DevOps == CALMS Culture Automation Lean Measure Share

Conway's Law - COBOL and ALGOL compiler (5 phases and 3 phases)
Operations can make developers far more productive


Key Areas:

    1. Reduce Org silos
    2. Accept failure as normal
    3. Implement gradual change
    4. Leverage tooling and automation
    5. Measure everything
    6. Keep workloads small and loosely coupled
    8. Deploy with automation
    9. Optimize for dev and ops
    10. Share responsibility
    11. Improve feedback loops
    12. Cultivate culture of learning
    13. Keep it simple
    14. Use data to make decisions
    15. Use feature flags for experimentation
    16. Use monitoring to detect problems