#  Copyright (c) 2015 - 2020, Intel Corporation. All rights reserved.<BR>
    def __init__(self, subject, message):
        self.check_signed_off_by()
        self.check_misc_signatures()
        self.check_overall_format()
                    self.filename.startswith('BaseTools/Bin/CYGWIN_NT-5.1-i686/') or \
        msg_check = CommitMessageCheck(self.commit_subject, self.commit_msg)