class JobProviders:

    def __init__(self, providers):
        self.offers = []
        self.providers = providers

    def getJobs(self):
        for provider_name in self.providers:
            provider = self.providers[provider_name]['class'](self.providers[provider_name]['endpoint'])

            self.offers.append(
                provider.getOffers()
            )
            
        return self.offers