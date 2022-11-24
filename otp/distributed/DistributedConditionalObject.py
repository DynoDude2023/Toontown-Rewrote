class DistributedConditionalObject(object):

    def shouldDisable(self):
        return False

    def updateRequiredOtherFields(self, dclass, di):
        # First, update the required fields
        dclass.receiveUpdateBroadcastRequired(self, di)

        if self.shouldDisable():
            self.disableAnnounceAndDelete()

            if self.doId in base.cr.doId2do:
                del base.cr.doId2do[self.doId]

            return

        # Announce generate after updating all the required fields,
        # but before we update the non-required fields.
        self.announceGenerate()
        self.postGenerateMessage()
        dclass.receiveUpdateOther(self, di)