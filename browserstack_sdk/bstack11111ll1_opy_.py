# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack111l1ll1_opy_
from browserstack_sdk.bstack1lll11ll1_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack111ll1ll_opy_
from bstack_utils.bstack1llll1l1l_opy_ import bstack111ll11l_opy_
from bstack_utils.constants import bstack1lll1ll11_opy_
from bstack_utils.bstack1111ll1l_opy_ import bstack1lll1111l_opy_
class bstack1llll1lll_opy_:
    def __init__(self, args, logger, bstack1llllllll_opy_, bstack1llll1111_opy_):
        self.args = args
        self.logger = logger
        self.bstack1llllllll_opy_ = bstack1llllllll_opy_
        self.bstack1llll1111_opy_ = bstack1llll1111_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1111l111_opy_ = []
        self.bstack1lll111l1_opy_ = []
        self.bstack111lll11_opy_ = []
        self.bstack1lll11l1l_opy_ = self.bstack1llll1ll1_opy_()
        self.bstack1lllll1ll_opy_ = -1
    def bstack1lll1l1ll_opy_(self, bstack11111111_opy_):
        self.parse_args()
        self.bstack111111ll_opy_()
        self.bstack11111l11_opy_(bstack11111111_opy_)
        self.bstack111l1111_opy_()
    def bstack111l111l_opy_(self):
        bstack1111ll1l_opy_ = bstack1lll1111l_opy_.bstack1llll111l_opy_(self.bstack1llllllll_opy_, self.logger)
        if bstack1111ll1l_opy_ is None:
            self.logger.warn(bstack11l11ll_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࠦࡩࡴࠢࡱࡳࡹࠦࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࡧ࠲࡙ࠥ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣৈ"))
            return
        bstack1llllll11_opy_ = False
        bstack1111ll1l_opy_.bstack1lll111ll_opy_(bstack11l11ll_opy_ (u"ࠨࡥ࡯ࡣࡥࡰࡪࡪࠢ৉"), bstack1111ll1l_opy_.bstack1lll1ll1l_opy_())
        start_time = time.time()
        if bstack1111ll1l_opy_.bstack1lll1ll1l_opy_():
            test_files = self.bstack1111l1l1_opy_()
            bstack1llllll11_opy_ = True
            bstack111l1l11_opy_ = bstack1111ll1l_opy_.bstack111111l1_opy_(test_files)
            if bstack111l1l11_opy_:
                self.bstack1111l111_opy_ = bstack111l1l11_opy_
                self.__1111l1ll_opy_()
                bstack1111ll1l_opy_.bstack1lll11l11_opy_(bstack1llllll11_opy_)
                self.logger.info(bstack11l11ll_opy_ (u"ࠢࡕࡧࡶࡸࡸࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡸࡷ࡮ࡴࡧࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧ৊").format(self.bstack1111l111_opy_))
            else:
                self.logger.info(bstack11l11ll_opy_ (u"ࠣࡐࡲࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡹࡨࡶࡪࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡥࡽࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨো"))
        bstack1111ll1l_opy_.bstack1lll111ll_opy_(bstack11l11ll_opy_ (u"ࠤࡷ࡭ࡲ࡫ࡔࡢ࡭ࡨࡲ࡙ࡵࡁࡱࡲ࡯ࡽࠧৌ"), int((time.time() - start_time) * 1000)) # bstack11111l1l_opy_ to bstack1111l11l_opy_
    def __1111l1ll_opy_(self):
        bstack11l11ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡳࡰࡦࡩࡥࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵࠣ࡭ࡳࠦࡃࡍࡋࠣࡪࡱࡧࡧࡴࠢࡺ࡭ࡹ࡮ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷࡩࡩࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡥࡳࡸࡨࡶࠥࡸࡥࡵࡷࡵࡲࡸࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡩ࡭ࡱ࡫ࠠ࡯ࡣࡰࡩࡸ࠲ࠠࡢࡰࡧࠤࡼ࡫ࠠࡴ࡫ࡰࡴࡱࡿࠠࡶࡲࡧࡥࡹ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡶ࡫ࡩࠥࡉࡌࡊࠢࡤࡶ࡬ࡹࠠࡵࡱࠣࡹࡸ࡫ࠠࡵࡪࡲࡷࡪࠦࡦࡪ࡮ࡨࡷ࠳ࠦࡕࡴࡧࡵࠫࡸࠦࡦࡪ࡮ࡷࡩࡷ࡯࡮ࡨࠢࡩࡰࡦ࡭ࡳࠡࠪ࠰ࡱ࠱ࠦ࠭࡬ࠫࠣࡶࡪࡳࡡࡪࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࡴࡢࡥࡷࠤࡦࡴࡤࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡤࡴࡵࡲࡩࡦࡦࠣࡲࡦࡺࡵࡳࡣ࡯ࡰࡾࠦࡤࡶࡴ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨ্ࠢࠣ")
        try:
            if not self.bstack1111l111_opy_:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡓࡵࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷࡩࡩࠦࡦࡪ࡮ࡨࡷࠥࡶࡡࡵࡪࠣࡸࡴࠦࡳࡦࡶࠥৎ"))
                return
            bstack11111lll_opy_ = []
            bstack1llll11ll_opy_ = []
            for flag in self.bstack1lll111l1_opy_:
                if flag.startswith(bstack11l11ll_opy_ (u"ࠬ࠳ࠧ৏")):
                    bstack11111lll_opy_.append(flag)
                    continue
                bstack1lll1l11l_opy_ = False
                if bstack11l11ll_opy_ (u"࠭࠺࠻ࠩ৐") in flag:
                    bstack1lll1l11l_opy_ = True
                elif os.path.exists(flag):
                    if os.path.isdir(flag) or (os.path.isfile(flag) and flag.endswith(bstack11l11ll_opy_ (u"ࠧ࠯ࡲࡼࠫ৑"))):
                        bstack1lll1l11l_opy_ = True
                if not bstack1lll1l11l_opy_:
                    bstack11111lll_opy_.append(flag)
                else:
                    bstack1llll11ll_opy_.append(flag)
            bstack11111lll_opy_.extend(self.bstack1111l111_opy_)
            self.bstack1lll111l1_opy_ = bstack11111lll_opy_
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡪࡺࡴࡪࡰࡪࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡦࡦࠣࡷࡪࡲࡥࡤࡶࡲࡶࡸࡀࠠࡼࡿࠥ৒").format(str(e)))
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1llllll1l_opy_():
        import importlib
        if getattr(importlib, bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡳࡪ࡟࡭ࡱࡤࡨࡪࡸࠧ৓"), False):
            bstack1lll1l111_opy_ = importlib.find_loader(bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ৔"))
        else:
            bstack1lll1l111_opy_ = importlib.util.find_spec(bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭৕"))
    def bstack1lllll111_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1lllll1ll_opy_ = -1
        if self.bstack1llll1111_opy_ and bstack11l11ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ৖") in self.bstack1llllllll_opy_:
            self.bstack1lllll1ll_opy_ = int(self.bstack1llllllll_opy_[bstack11l11ll_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ৗ")])
        try:
            bstack1lllll11l_opy_ = [bstack11l11ll_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩ৘"), bstack11l11ll_opy_ (u"ࠨ࠯࠰ࡴࡱࡻࡧࡪࡰࡶࠫ৙"), bstack11l11ll_opy_ (u"ࠩ࠰ࡴࠬ৚")]
            if self.bstack1lllll1ll_opy_ >= 0:
                bstack1lllll11l_opy_.extend([bstack11l11ll_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ৛"), bstack11l11ll_opy_ (u"ࠫ࠲ࡴࠧড়")])
            for arg in bstack1lllll11l_opy_:
                self.bstack1lllll111_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111111ll_opy_(self):
        bstack1lll111l1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1lll111l1_opy_ = bstack1lll111l1_opy_
        return self.bstack1lll111l1_opy_
    def bstack1llll11l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1llllll1l_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack111ll1ll_opy_)
    def bstack11111l11_opy_(self, bstack11111111_opy_):
        bstack1lll11111_opy_ = Config.bstack1llll111l_opy_()
        if bstack11111111_opy_:
            self.bstack1lll111l1_opy_.append(bstack11l11ll_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩঢ়"))
            self.bstack1lll111l1_opy_.append(bstack11l11ll_opy_ (u"࠭ࡔࡳࡷࡨࠫ৞"))
        if bstack1lll11111_opy_.bstack1lllllll1_opy_():
            self.bstack1lll111l1_opy_.append(bstack11l11ll_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭য়"))
            self.bstack1lll111l1_opy_.append(bstack11l11ll_opy_ (u"ࠨࡖࡵࡹࡪ࠭ৠ"))
        self.bstack1lll111l1_opy_.append(bstack11l11ll_opy_ (u"ࠩ࠰ࡴࠬৡ"))
        self.bstack1lll111l1_opy_.append(bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠨৢ"))
        self.bstack1lll111l1_opy_.append(bstack11l11ll_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭ৣ"))
        self.bstack1lll111l1_opy_.append(bstack11l11ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ৤"))
        if self.bstack1lllll1ll_opy_ > 1:
            self.bstack1lll111l1_opy_.append(bstack11l11ll_opy_ (u"࠭࠭࡯ࠩ৥"))
            self.bstack1lll111l1_opy_.append(str(self.bstack1lllll1ll_opy_))
    def bstack111l1111_opy_(self):
        if bstack111ll11l_opy_.bstack111ll111_opy_(self.bstack1llllllll_opy_):
             self.bstack1lll111l1_opy_ += [
                bstack1lll1ll11_opy_.get(bstack11l11ll_opy_ (u"ࠧࡳࡧࡵࡹࡳ࠭০")), str(bstack111ll11l_opy_.bstack1lll1l1l1_opy_(self.bstack1llllllll_opy_)),
                bstack1lll1ll11_opy_.get(bstack11l11ll_opy_ (u"ࠨࡦࡨࡰࡦࡿࠧ১")), str(bstack1lll1ll11_opy_.get(bstack11l11ll_opy_ (u"ࠩࡵࡩࡷࡻ࡮࠮ࡦࡨࡰࡦࡿࠧ২")))
            ]
    def bstack111l1l1l_opy_(self):
        bstack111lll11_opy_ = []
        for spec in self.bstack1111l111_opy_:
            bstack111ll1l1_opy_ = [spec]
            bstack111ll1l1_opy_ += self.bstack1lll111l1_opy_
            bstack111lll11_opy_.append(bstack111ll1l1_opy_)
        self.bstack111lll11_opy_ = bstack111lll11_opy_
        return bstack111lll11_opy_
    def bstack1llll1ll1_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1lll11l1l_opy_ = True
            return True
        except Exception as e:
            self.bstack1lll11l1l_opy_ = False
        return self.bstack1lll11l1l_opy_
    def bstack1lll1lll1_opy_(self):
        bstack11l11ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡈࡧࡷࠤࡹ࡮ࡥࠡࡥࡲࡹࡳࡺࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡹ࡮ࡥ࡮ࠢࡸࡷ࡮ࡴࡧࠡࡲࡼࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡪࡰࡷ࠾࡚ࠥࡨࡦࠢࡷࡳࡹࡧ࡬ࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ৩")
        try:
            from browserstack_sdk.bstack11ll1l1l_opy_ import bstack11ll11ll_opy_
            bstack1lll1llll_opy_ = bstack11ll11ll_opy_(bstack11ll11l1_opy_=self.bstack1lll111l1_opy_)
            if not bstack1lll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ৪"), False):
                self.logger.error(bstack11l11ll_opy_ (u"࡚ࠧࡥࡴࡶࠣࡧࡴࡻ࡮ࡵࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠥ৫").format(bstack1lll1llll_opy_.get(bstack11l11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ৬"), bstack11l11ll_opy_ (u"ࠧࡖࡰ࡮ࡲࡴࡽ࡮ࠡࡧࡵࡶࡴࡸࠧ৭"))))
                return 0
            count = bstack1lll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠨࡥࡲࡹࡳࡺࠧ৮"), 0)
            test_files = bstack1lll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸ࠭৯"), [])
            self.logger.info(bstack11l11ll_opy_ (u"ࠥࡘࡴࡺࡡ࡭ࠢࡷࡩࡸࡺࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧ࠾ࠥࢁࡽࠣৰ").format(count))
            return count
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽࠣৱ").format(e))
            return 0
    def bstack1lll11lll_opy_(self, bstack111l1lll_opy_, bstack1lll1l1ll_opy_):
        bstack1lll1l1ll_opy_[bstack11l11ll_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ৲")] = self.bstack1llllllll_opy_
        multiprocessing.set_start_method(bstack11l11ll_opy_ (u"࠭ࡳࡱࡣࡺࡲࠬ৳"))
        bstack111l11ll_opy_ = []
        manager = multiprocessing.Manager()
        bstack1111ll11_opy_ = manager.list()
        if bstack11l11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৴") in self.bstack1llllllll_opy_:
            for index, platform in enumerate(self.bstack1llllllll_opy_[bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ৵")]):
                bstack111l11ll_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack111l1lll_opy_,
                                                            args=(self.bstack1lll111l1_opy_, bstack1lll1l1ll_opy_, bstack1111ll11_opy_)))
            bstack1lllll1l1_opy_ = len(self.bstack1llllllll_opy_[bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৶")])
        else:
            bstack111l11ll_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack111l1lll_opy_,
                                                        args=(self.bstack1lll111l1_opy_, bstack1lll1l1ll_opy_, bstack1111ll11_opy_)))
            bstack1lllll1l1_opy_ = 1
        i = 0
        for t in bstack111l11ll_opy_:
            os.environ[bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ৷")] = str(i)
            if bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ৸") in self.bstack1llllllll_opy_:
                os.environ[bstack11l11ll_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭৹")] = json.dumps(self.bstack1llllllll_opy_[bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৺")][i % bstack1lllll1l1_opy_])
            i += 1
            t.start()
        for t in bstack111l11ll_opy_:
            t.join()
        return list(bstack1111ll11_opy_)
    @staticmethod
    def bstack111l11l1_opy_(driver, bstack1111111l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ৻"), None)
        if item and getattr(item, bstack11l11ll_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࠪৼ"), None) and not getattr(item, bstack11l11ll_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡳࡵࡥࡤࡰࡰࡨࠫ৽"), False):
            logger.info(
                bstack11l11ll_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠤ৾"))
            bstack1llll1l11_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack111l1ll1_opy_.bstack1111llll_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1111l1l1_opy_(self):
        bstack11l11ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡹࡵࠠࡣࡧࠣࡩࡽ࡫ࡣࡶࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ৿")
        try:
            from browserstack_sdk.bstack11ll1l1l_opy_ import bstack11ll11ll_opy_
            bstack1111lll1_opy_ = bstack11ll11ll_opy_(bstack11ll11l1_opy_=self.bstack1lll111l1_opy_)
            if not bstack1111lll1_opy_.get(bstack11l11ll_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭਀"), False):
                self.logger.error(bstack11l11ll_opy_ (u"ࠨࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠥਁ").format(bstack1111lll1_opy_.get(bstack11l11ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ਂ"), bstack11l11ll_opy_ (u"ࠨࡗࡱ࡯ࡳࡵࡷ࡯ࠢࡨࡶࡷࡵࡲࠨਃ"))))
                return []
            test_files = bstack1111lll1_opy_.get(bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸ࠭਄"), [])
            count = bstack1111lll1_opy_.get(bstack11l11ll_opy_ (u"ࠪࡧࡴࡻ࡮ࡵࠩਅ"), 0)
            self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸࡪࡪࠠࡼࡿࠣࡸࡪࡹࡴࡴࠢ࡬ࡲࠥࢁࡽࠡࡨ࡬ࡰࡪࡹࠢਆ").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡦࡸࡶ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯࠼ࠣࡿࢂࠨਇ").format(e))
            return []