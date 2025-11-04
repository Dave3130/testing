# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1111111l_opy_
from browserstack_sdk.bstack1111llll_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1llllll1l_opy_
from bstack_utils.bstack1llllll11_opy_ import bstack1lllllll1_opy_
from bstack_utils.constants import bstack1111l111_opy_
from bstack_utils.bstack1111ll11_opy_ import bstack1lll1ll11_opy_
class bstack1lllll111_opy_:
    def __init__(self, args, logger, bstack111ll11l_opy_, bstack1lll1l1l1_opy_):
        self.args = args
        self.logger = logger
        self.bstack111ll11l_opy_ = bstack111ll11l_opy_
        self.bstack1lll1l1l1_opy_ = bstack1lll1l1l1_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11111l1l_opy_ = []
        self.bstack1llll1lll_opy_ = []
        self.bstack111l1l11_opy_ = []
        self.bstack1lllll11l_opy_ = self.bstack111ll1ll_opy_()
        self.bstack111lll1l_opy_ = -1
    def bstack1111ll1l_opy_(self, bstack1lll1ll1l_opy_):
        self.parse_args()
        self.bstack1llll1111_opy_()
        self.bstack111l1ll1_opy_(bstack1lll1ll1l_opy_)
        self.bstack1llll1ll1_opy_()
    def bstack1lll1lll1_opy_(self):
        bstack1111ll11_opy_ = bstack1lll1ll11_opy_.bstack1llllllll_opy_(self.bstack111ll11l_opy_, self.logger)
        if bstack1111ll11_opy_ is None:
            self.logger.warn(bstack11l1111_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࠦࡩࡴࠢࡱࡳࡹࠦࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࡧ࠲࡙ࠥ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣৈ"))
            return
        bstack111111ll_opy_ = False
        bstack1111ll11_opy_.bstack1llll111l_opy_(bstack11l1111_opy_ (u"ࠨࡥ࡯ࡣࡥࡰࡪࡪࠢ৉"), bstack1111ll11_opy_.bstack1111lll1_opy_())
        start_time = time.time()
        if bstack1111ll11_opy_.bstack1111lll1_opy_():
            test_files = self.bstack111l11l1_opy_()
            bstack111111ll_opy_ = True
            bstack11111l11_opy_ = bstack1111ll11_opy_.bstack1lll11l1l_opy_(test_files)
            if bstack11111l11_opy_:
                self.bstack11111l1l_opy_ = bstack11111l11_opy_
                self.__1lll1l1ll_opy_()
                bstack1111ll11_opy_.bstack111lll11_opy_(bstack111111ll_opy_)
                self.logger.info(bstack11l1111_opy_ (u"ࠢࡕࡧࡶࡸࡸࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡸࡷ࡮ࡴࡧࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧ৊").format(self.bstack11111l1l_opy_))
            else:
                self.logger.info(bstack11l1111_opy_ (u"ࠣࡐࡲࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡹࡨࡶࡪࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡥࡽࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨো"))
        bstack1111ll11_opy_.bstack1llll111l_opy_(bstack11l1111_opy_ (u"ࠤࡷ࡭ࡲ࡫ࡔࡢ࡭ࡨࡲ࡙ࡵࡁࡱࡲ࡯ࡽࠧৌ"), int((time.time() - start_time) * 1000)) # bstack111l11ll_opy_ to bstack111ll111_opy_
    def __1lll1l1ll_opy_(self):
        bstack11l1111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡳࡰࡦࡩࡥࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵࠣ࡭ࡳࠦࡃࡍࡋࠣࡪࡱࡧࡧࡴࠢࡺ࡭ࡹ࡮ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷࡩࡩࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡥࡳࡸࡨࡶࠥࡸࡥࡵࡷࡵࡲࡸࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡩ࡭ࡱ࡫ࠠ࡯ࡣࡰࡩࡸ࠲ࠠࡢࡰࡧࠤࡼ࡫ࠠࡴ࡫ࡰࡴࡱࡿࠠࡶࡲࡧࡥࡹ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡶ࡫ࡩࠥࡉࡌࡊࠢࡤࡶ࡬ࡹࠠࡵࡱࠣࡹࡸ࡫ࠠࡵࡪࡲࡷࡪࠦࡦࡪ࡮ࡨࡷ࠳ࠦࡕࡴࡧࡵࠫࡸࠦࡦࡪ࡮ࡷࡩࡷ࡯࡮ࡨࠢࡩࡰࡦ࡭ࡳࠡࠪ࠰ࡱ࠱ࠦ࠭࡬ࠫࠣࡶࡪࡳࡡࡪࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࡴࡢࡥࡷࠤࡦࡴࡤࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡤࡴࡵࡲࡩࡦࡦࠣࡲࡦࡺࡵࡳࡣ࡯ࡰࡾࠦࡤࡶࡴ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨ্ࠢࠣ")
        try:
            if not self.bstack11111l1l_opy_:
                self.logger.debug(bstack11l1111_opy_ (u"ࠦࡓࡵࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷࡩࡩࠦࡦࡪ࡮ࡨࡷࠥࡶࡡࡵࡪࠣࡸࡴࠦࡳࡦࡶࠥৎ"))
                return
            bstack111111l1_opy_ = []
            for flag in self.bstack1llll1lll_opy_:
                if flag.startswith(bstack11l1111_opy_ (u"ࠬ࠳ࠧ৏")):
                    bstack111111l1_opy_.append(flag)
                    continue
                bstack1111l1ll_opy_ = False
                if bstack11l1111_opy_ (u"࠭࠺࠻ࠩ৐") in flag:
                    bstack11111111_opy_ = flag.split(bstack11l1111_opy_ (u"ࠧ࠻࠼ࠪ৑"), 1)[0]
                    if os.path.exists(bstack11111111_opy_):
                        bstack1111l1ll_opy_ = True
                elif os.path.exists(flag):
                    if os.path.isdir(flag) or (os.path.isfile(flag) and flag.endswith(bstack11l1111_opy_ (u"ࠨ࠰ࡳࡽࠬ৒"))):
                        bstack1111l1ll_opy_ = True
                if not bstack1111l1ll_opy_:
                    bstack111111l1_opy_.append(flag)
            bstack111111l1_opy_.extend(self.bstack11111l1l_opy_)
            self.bstack1llll1lll_opy_ = bstack111111l1_opy_
        except Exception as e:
            self.logger.error(bstack11l1111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵࡧࡧࠤࡸ࡫࡬ࡦࡥࡷࡳࡷࡹ࠺ࠡࡽࢀࠦ৓").format(str(e)))
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111l1lll_opy_():
        import importlib
        if getattr(importlib, bstack11l1111_opy_ (u"ࠪࡪ࡮ࡴࡤࡠ࡮ࡲࡥࡩ࡫ࡲࠨ৔"), False):
            bstack1111l11l_opy_ = importlib.find_loader(bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭৕"))
        else:
            bstack1111l11l_opy_ = importlib.util.find_spec(bstack11l1111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ৖"))
    def bstack1llll11l1_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack111lll1l_opy_ = -1
        if self.bstack1lll1l1l1_opy_ and bstack11l1111_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ৗ") in self.bstack111ll11l_opy_:
            self.bstack111lll1l_opy_ = int(self.bstack111ll11l_opy_[bstack11l1111_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ৘")])
        try:
            bstack1lll1111l_opy_ = [bstack11l1111_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪ৙"), bstack11l1111_opy_ (u"ࠩ࠰࠱ࡵࡲࡵࡨ࡫ࡱࡷࠬ৚"), bstack11l1111_opy_ (u"ࠪ࠱ࡵ࠭৛")]
            if self.bstack111lll1l_opy_ >= 0:
                bstack1lll1111l_opy_.extend([bstack11l1111_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬড়"), bstack11l1111_opy_ (u"ࠬ࠳࡮ࠨঢ়")])
            for arg in bstack1lll1111l_opy_:
                self.bstack1llll11l1_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1llll1111_opy_(self):
        bstack1llll1lll_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1llll1lll_opy_ = bstack1llll1lll_opy_
        return self.bstack1llll1lll_opy_
    def bstack111l111l_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111l1lll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1llllll1l_opy_)
    def bstack111l1ll1_opy_(self, bstack1lll1ll1l_opy_):
        bstack1llll11ll_opy_ = Config.bstack1llllllll_opy_()
        if bstack1lll1ll1l_opy_:
            self.bstack1llll1lll_opy_.append(bstack11l1111_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ৞"))
            self.bstack1llll1lll_opy_.append(bstack11l1111_opy_ (u"ࠧࡕࡴࡸࡩࠬয়"))
        if bstack1llll11ll_opy_.bstack111ll1l1_opy_():
            self.bstack1llll1lll_opy_.append(bstack11l1111_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧৠ"))
            self.bstack1llll1lll_opy_.append(bstack11l1111_opy_ (u"ࠩࡗࡶࡺ࡫ࠧৡ"))
        self.bstack1llll1lll_opy_.append(bstack11l1111_opy_ (u"ࠪ࠱ࡵ࠭ৢ"))
        self.bstack1llll1lll_opy_.append(bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠩৣ"))
        self.bstack1llll1lll_opy_.append(bstack11l1111_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧ৤"))
        self.bstack1llll1lll_opy_.append(bstack11l1111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭৥"))
        if self.bstack111lll1l_opy_ > 1:
            self.bstack1llll1lll_opy_.append(bstack11l1111_opy_ (u"ࠧ࠮ࡰࠪ০"))
            self.bstack1llll1lll_opy_.append(str(self.bstack111lll1l_opy_))
    def bstack1llll1ll1_opy_(self):
        if bstack1lllllll1_opy_.bstack1lll1llll_opy_(self.bstack111ll11l_opy_):
             self.bstack1llll1lll_opy_ += [
                bstack1111l111_opy_.get(bstack11l1111_opy_ (u"ࠨࡴࡨࡶࡺࡴࠧ১")), str(bstack1lllllll1_opy_.bstack1lll111ll_opy_(self.bstack111ll11l_opy_)),
                bstack1111l111_opy_.get(bstack11l1111_opy_ (u"ࠩࡧࡩࡱࡧࡹࠨ২")), str(bstack1111l111_opy_.get(bstack11l1111_opy_ (u"ࠪࡶࡪࡸࡵ࡯࠯ࡧࡩࡱࡧࡹࠨ৩")))
            ]
    def bstack111l1l1l_opy_(self):
        bstack111l1l11_opy_ = []
        for spec in self.bstack11111l1l_opy_:
            bstack1llll1l11_opy_ = [spec]
            bstack1llll1l11_opy_ += self.bstack1llll1lll_opy_
            bstack111l1l11_opy_.append(bstack1llll1l11_opy_)
        self.bstack111l1l11_opy_ = bstack111l1l11_opy_
        return bstack111l1l11_opy_
    def bstack111ll1ll_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1lllll11l_opy_ = True
            return True
        except Exception as e:
            self.bstack1lllll11l_opy_ = False
        return self.bstack1lllll11l_opy_
    def bstack1lllll1ll_opy_(self):
        bstack11l1111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡉࡨࡸࠥࡺࡨࡦࠢࡦࡳࡺࡴࡴࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࡻ࡮ࡺࡨࡰࡷࡷࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡺࡨࡦ࡯ࠣࡹࡸ࡯࡮ࡨࠢࡳࡽࡹ࡫ࡳࡵࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡱࡸ࠿ࠦࡔࡩࡧࠣࡸࡴࡺࡡ࡭ࠢࡱࡹࡲࡨࡥࡳࠢࡲࡪࠥࡺࡥࡴࡶࡶࠤࡨࡵ࡬࡭ࡧࡦࡸࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ৪")
        try:
            from browserstack_sdk.bstack11l1lll1_opy_ import bstack11l1ll1l_opy_
            bstack1lll1l11l_opy_ = bstack11l1ll1l_opy_(bstack11ll111l_opy_=self.bstack1llll1lll_opy_)
            if not bstack1lll1l11l_opy_.get(bstack11l1111_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭৫"), False):
                self.logger.error(bstack11l1111_opy_ (u"ࠨࡔࡦࡵࡷࠤࡨࡵࡵ࡯ࡶࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪ࠺ࠡࡽࢀࠦ৬").format(bstack1lll1l11l_opy_.get(bstack11l1111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭৭"), bstack11l1111_opy_ (u"ࠨࡗࡱ࡯ࡳࡵࡷ࡯ࠢࡨࡶࡷࡵࡲࠨ৮"))))
                return 0
            count = bstack1lll1l11l_opy_.get(bstack11l1111_opy_ (u"ࠩࡦࡳࡺࡴࡴࠨ৯"), 0)
            self.logger.info(bstack11l1111_opy_ (u"ࠥࡘࡴࡺࡡ࡭ࠢࡷࡩࡸࡺࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧ࠾ࠥࢁࡽࠣৰ").format(count))
            return count
        except Exception as e:
            self.logger.error(bstack11l1111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽࠣৱ").format(e))
            return 0
    def bstack1lll11lll_opy_(self, bstack1lll11l11_opy_, bstack1111ll1l_opy_):
        bstack1111ll1l_opy_[bstack11l1111_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ৲")] = self.bstack111ll11l_opy_
        multiprocessing.set_start_method(bstack11l1111_opy_ (u"࠭ࡳࡱࡣࡺࡲࠬ৳"))
        bstack1lll111l1_opy_ = []
        manager = multiprocessing.Manager()
        bstack11111lll_opy_ = manager.list()
        if bstack11l1111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৴") in self.bstack111ll11l_opy_:
            for index, platform in enumerate(self.bstack111ll11l_opy_[bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ৵")]):
                bstack1lll111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1lll11l11_opy_,
                                                            args=(self.bstack1llll1lll_opy_, bstack1111ll1l_opy_, bstack11111lll_opy_)))
            bstack1lll11ll1_opy_ = len(self.bstack111ll11l_opy_[bstack11l1111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৶")])
        else:
            bstack1lll111l1_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1lll11l11_opy_,
                                                        args=(self.bstack1llll1lll_opy_, bstack1111ll1l_opy_, bstack11111lll_opy_)))
            bstack1lll11ll1_opy_ = 1
        i = 0
        for t in bstack1lll111l1_opy_:
            os.environ[bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ৷")] = str(i)
            if bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ৸") in self.bstack111ll11l_opy_:
                os.environ[bstack11l1111_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭৹")] = json.dumps(self.bstack111ll11l_opy_[bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৺")][i % bstack1lll11ll1_opy_])
            i += 1
            t.start()
        for t in bstack1lll111l1_opy_:
            t.join()
        return list(bstack11111lll_opy_)
    @staticmethod
    def bstack1llll1l1l_opy_(driver, bstack111l1111_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11l1111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ৻"), None)
        if item and getattr(item, bstack11l1111_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࠪৼ"), None) and not getattr(item, bstack11l1111_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡳࡵࡥࡤࡰࡰࡨࠫ৽"), False):
            logger.info(
                bstack11l1111_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠤ৾"))
            bstack11111ll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1111111l_opy_.bstack1lll1l111_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack111l11l1_opy_(self):
        bstack11l1111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡹࡵࠠࡣࡧࠣࡩࡽ࡫ࡣࡶࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ৿")
        try:
            from browserstack_sdk.bstack11l1lll1_opy_ import bstack11l1ll1l_opy_
            bstack1lllll1l1_opy_ = bstack11l1ll1l_opy_(bstack11ll111l_opy_=self.bstack1llll1lll_opy_)
            if not bstack1lllll1l1_opy_.get(bstack11l1111_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭਀"), False):
                self.logger.error(bstack11l1111_opy_ (u"ࠨࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠥਁ").format(bstack1lllll1l1_opy_.get(bstack11l1111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ਂ"), bstack11l1111_opy_ (u"ࠨࡗࡱ࡯ࡳࡵࡷ࡯ࠢࡨࡶࡷࡵࡲࠨਃ"))))
                return []
            test_files = bstack1lllll1l1_opy_.get(bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸ࠭਄"), [])
            count = bstack1lllll1l1_opy_.get(bstack11l1111_opy_ (u"ࠪࡧࡴࡻ࡮ࡵࠩਅ"), 0)
            self.logger.debug(bstack11l1111_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸࡪࡪࠠࡼࡿࠣࡸࡪࡹࡴࡴࠢ࡬ࡲࠥࢁࡽࠡࡨ࡬ࡰࡪࡹࠢਆ").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l1111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡦࡸࡶ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯࠼ࠣࡿࢂࠨਇ").format(e))
            return []