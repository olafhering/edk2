#  Copyright (c) 2015 - 2021, Intel Corporation. All rights reserved.<BR>
    def __init__(self, subject, message, author_email):
        MergifyMerge = False
        if "mergify[bot]@users.noreply.github.com" in author_email:
            if "Merge branch" in subject:
                MergifyMerge = True

        if not MergifyMerge:
            self.check_signed_off_by()
            self.check_misc_signatures()
            self.check_overall_format()
                if os.path.basename(self.filename) == 'GNUmakefile' or \
                   os.path.basename(self.filename).lower() == 'makefile' or \
                   os.path.splitext(self.filename)[1] == '.makefile' or \
                   self.filename.startswith(
                        'BaseTools/Source/C/VfrCompile/Pccts/'):
                    self.force_notabs = False
        rp_file = os.path.realpath(self.filename)
        rp_script = os.path.realpath(__file__)
        if line.find('__FUNCTION__') != -1 and rp_file != rp_script:
            self.added_line_error('__FUNCTION__ was used, but __func__ '
                                  'is now recommended', line)

        msg_check = CommitMessageCheck(self.commit_subject, self.commit_msg, self.author_email)