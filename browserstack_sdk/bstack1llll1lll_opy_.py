# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1lllll1l1_opy_
from browserstack_sdk.bstack1lll1ll11_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1111ll1l_opy_
from bstack_utils.bstack111l1111_opy_ import bstack1llllll11_opy_
from bstack_utils.constants import bstack1111ll11_opy_
from bstack_utils.bstack1llllllll_opy_ import bstack1lll1l11l_opy_
class bstack1111llll_opy_:
    def __init__(self, args, logger, bstack1llll1l1l_opy_, bstack1lll11ll1_opy_):
        self.args = args
        self.logger = logger
        self.bstack1llll1l1l_opy_ = bstack1llll1l1l_opy_
        self.bstack1lll11ll1_opy_ = bstack1lll11ll1_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11111l11_opy_ = []
        self.bstack11111ll1_opy_ = []
        self.bstack1lll1l1ll_opy_ = []
        self.bstack1111lll1_opy_ = self.bstack11111111_opy_()
        self.bstack1111l111_opy_ = -1
    def bstack111ll11l_opy_(self, bstack1111l1ll_opy_):
        self.parse_args()
        self.bstack1llll1l11_opy_()
        self.bstack1llll1111_opy_(bstack1111l1ll_opy_)
        self.bstack111ll111_opy_()
    def bstack111l1l11_opy_(self):
        bstack1llllllll_opy_ = bstack1lll1l11l_opy_.bstack111111ll_opy_(self.bstack1llll1l1l_opy_, self.logger)
        if bstack1llllllll_opy_ is None:
            self.logger.warn(bstack11ll1l_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࠦࡩࡴࠢࡱࡳࡹࠦࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࡧ࠲࡙ࠥ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣৈ"))
            return
        bstack111ll1ll_opy_ = False
        bstack1llllllll_opy_.bstack11111lll_opy_(bstack11ll1l_opy_ (u"ࠨࡥ࡯ࡣࡥࡰࡪࡪࠢ৉"), bstack1llllllll_opy_.bstack1lll11l1l_opy_())
        start_time = time.time()
        if bstack1llllllll_opy_.bstack1lll11l1l_opy_():
            test_files = self.bstack111l1ll1_opy_()
            bstack111ll1ll_opy_ = True
            bstack1lll1ll1l_opy_ = bstack1llllllll_opy_.bstack1111111l_opy_(test_files)
            if bstack1lll1ll1l_opy_:
                self.bstack11111l11_opy_ = bstack1lll1ll1l_opy_
                self.__1lll1111l_opy_()
                bstack1llllllll_opy_.bstack111l1lll_opy_(bstack111ll1ll_opy_)
                self.logger.info(bstack11ll1l_opy_ (u"ࠢࡕࡧࡶࡸࡸࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡸࡷ࡮ࡴࡧࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧ৊").format(self.bstack11111l11_opy_))
            else:
                self.logger.info(bstack11ll1l_opy_ (u"ࠣࡐࡲࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡹࡨࡶࡪࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡥࡽࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨো"))
        bstack1llllllll_opy_.bstack11111lll_opy_(bstack11ll1l_opy_ (u"ࠤࡷ࡭ࡲ࡫ࡔࡢ࡭ࡨࡲ࡙ࡵࡁࡱࡲ࡯ࡽࠧৌ"), int((time.time() - start_time) * 1000)) # bstack1lll11l11_opy_ to bstack1111l11l_opy_
    def __1lll1111l_opy_(self):
        bstack11ll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡳࡰࡦࡩࡥࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵࠣ࡭ࡳࠦࡃࡍࡋࠣࡪࡱࡧࡧࡴࠢࡺ࡭ࡹ࡮ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷࡩࡩࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡥࡳࡸࡨࡶࠥࡸࡥࡵࡷࡵࡲࡸࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡩ࡭ࡱ࡫ࠠ࡯ࡣࡰࡩࡸ࠲ࠠࡢࡰࡧࠤࡼ࡫ࠠࡴ࡫ࡰࡴࡱࡿࠠࡶࡲࡧࡥࡹ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡶ࡫ࡩࠥࡉࡌࡊࠢࡤࡶ࡬ࡹࠠࡵࡱࠣࡹࡸ࡫ࠠࡵࡪࡲࡷࡪࠦࡦࡪ࡮ࡨࡷ࠳ࠦࡕࡴࡧࡵࠫࡸࠦࡦࡪ࡮ࡷࡩࡷ࡯࡮ࡨࠢࡩࡰࡦ࡭ࡳࠡࠪ࠰ࡱ࠱ࠦ࠭࡬ࠫࠣࡶࡪࡳࡡࡪࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࡴࡢࡥࡷࠤࡦࡴࡤࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡤࡴࡵࡲࡩࡦࡦࠣࡲࡦࡺࡵࡳࡣ࡯ࡰࡾࠦࡤࡶࡴ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨ্ࠢࠣ")
        try:
            if not self.bstack11111l11_opy_:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡓࡵࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷࡩࡩࠦࡦࡪ࡮ࡨࡷࠥࡶࡡࡵࡪࠣࡸࡴࠦࡳࡦࡶࠥৎ"))
                return
            bstack111l11l1_opy_ = []
            bstack11111l1l_opy_ = []
            for flag in self.bstack11111ll1_opy_:
                if flag.startswith(bstack11ll1l_opy_ (u"ࠬ࠳ࠧ৏")):
                    bstack111l11l1_opy_.append(flag)
                    continue
                bstack1lll11lll_opy_ = False
                if bstack11ll1l_opy_ (u"࠭࠺࠻ࠩ৐") in flag:
                    bstack1lll11lll_opy_ = True
                elif os.path.exists(flag):
                    if os.path.isdir(flag) or (os.path.isfile(flag) and flag.endswith(bstack11ll1l_opy_ (u"ࠧ࠯ࡲࡼࠫ৑"))):
                        bstack1lll11lll_opy_ = True
                if not bstack1lll11lll_opy_:
                    bstack111l11l1_opy_.append(flag)
                else:
                    bstack11111l1l_opy_.append(flag)
            bstack111l11l1_opy_.extend(self.bstack11111l11_opy_)
            self.bstack11111ll1_opy_ = bstack111l11l1_opy_
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡪࡺࡴࡪࡰࡪࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡦࡦࠣࡷࡪࡲࡥࡤࡶࡲࡶࡸࡀࠠࡼࡿࠥ৒").format(str(e)))
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111111l1_opy_():
        import importlib
        if getattr(importlib, bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡳࡪ࡟࡭ࡱࡤࡨࡪࡸࠧ৓"), False):
            bstack111l11ll_opy_ = importlib.find_loader(bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ৔"))
        else:
            bstack111l11ll_opy_ = importlib.util.find_spec(bstack11ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭৕"))
    def bstack111l111l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1111l111_opy_ = -1
        if self.bstack1lll11ll1_opy_ and bstack11ll1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ৖") in self.bstack1llll1l1l_opy_:
            self.bstack1111l111_opy_ = int(self.bstack1llll1l1l_opy_[bstack11ll1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ৗ")])
        try:
            bstack1llll11ll_opy_ = [bstack11ll1l_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩ৘"), bstack11ll1l_opy_ (u"ࠨ࠯࠰ࡴࡱࡻࡧࡪࡰࡶࠫ৙"), bstack11ll1l_opy_ (u"ࠩ࠰ࡴࠬ৚")]
            if self.bstack1111l111_opy_ >= 0:
                bstack1llll11ll_opy_.extend([bstack11ll1l_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ৛"), bstack11ll1l_opy_ (u"ࠫ࠲ࡴࠧড়")])
            for arg in bstack1llll11ll_opy_:
                self.bstack111l111l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1llll1l11_opy_(self):
        bstack11111ll1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11111ll1_opy_ = bstack11111ll1_opy_
        return self.bstack11111ll1_opy_
    def bstack1111l1l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111111l1_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1111ll1l_opy_)
    def bstack1llll1111_opy_(self, bstack1111l1ll_opy_):
        bstack111ll1l1_opy_ = Config.bstack111111ll_opy_()
        if bstack1111l1ll_opy_:
            self.bstack11111ll1_opy_.append(bstack11ll1l_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩঢ়"))
            self.bstack11111ll1_opy_.append(bstack11ll1l_opy_ (u"࠭ࡔࡳࡷࡨࠫ৞"))
        if bstack111ll1l1_opy_.bstack1lll1lll1_opy_():
            self.bstack11111ll1_opy_.append(bstack11ll1l_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭য়"))
            self.bstack11111ll1_opy_.append(bstack11ll1l_opy_ (u"ࠨࡖࡵࡹࡪ࠭ৠ"))
        self.bstack11111ll1_opy_.append(bstack11ll1l_opy_ (u"ࠩ࠰ࡴࠬৡ"))
        self.bstack11111ll1_opy_.append(bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠨৢ"))
        self.bstack11111ll1_opy_.append(bstack11ll1l_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭ৣ"))
        self.bstack11111ll1_opy_.append(bstack11ll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ৤"))
        if self.bstack1111l111_opy_ > 1:
            self.bstack11111ll1_opy_.append(bstack11ll1l_opy_ (u"࠭࠭࡯ࠩ৥"))
            self.bstack11111ll1_opy_.append(str(self.bstack1111l111_opy_))
    def bstack111ll111_opy_(self):
        if bstack1llllll11_opy_.bstack1lllll111_opy_(self.bstack1llll1l1l_opy_):
             self.bstack11111ll1_opy_ += [
                bstack1111ll11_opy_.get(bstack11ll1l_opy_ (u"ࠧࡳࡧࡵࡹࡳ࠭০")), str(bstack1llllll11_opy_.bstack1lllllll1_opy_(self.bstack1llll1l1l_opy_)),
                bstack1111ll11_opy_.get(bstack11ll1l_opy_ (u"ࠨࡦࡨࡰࡦࡿࠧ১")), str(bstack1111ll11_opy_.get(bstack11ll1l_opy_ (u"ࠩࡵࡩࡷࡻ࡮࠮ࡦࡨࡰࡦࡿࠧ২")))
            ]
    def bstack1lll11111_opy_(self):
        bstack1lll1l1ll_opy_ = []
        for spec in self.bstack11111l11_opy_:
            bstack1llll11l1_opy_ = [spec]
            bstack1llll11l1_opy_ += self.bstack11111ll1_opy_
            bstack1lll1l1ll_opy_.append(bstack1llll11l1_opy_)
        self.bstack1lll1l1ll_opy_ = bstack1lll1l1ll_opy_
        return bstack1lll1l1ll_opy_
    def bstack11111111_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1111lll1_opy_ = True
            return True
        except Exception as e:
            self.bstack1111lll1_opy_ = False
        return self.bstack1111lll1_opy_
    def bstack1lll111l1_opy_(self):
        bstack11ll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡈࡧࡷࠤࡹ࡮ࡥࠡࡥࡲࡹࡳࡺࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡹ࡮ࡥ࡮ࠢࡸࡷ࡮ࡴࡧࠡࡲࡼࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡪࡰࡷ࠾࡚ࠥࡨࡦࠢࡷࡳࡹࡧ࡬ࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ৩")
        try:
            from browserstack_sdk.bstack11l1lll1_opy_ import bstack11ll1111_opy_
            bstack1lllll1ll_opy_ = bstack11ll1111_opy_(bstack11ll1l11_opy_=self.bstack11111ll1_opy_)
            if not bstack1lllll1ll_opy_.get(bstack11ll1l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ৪"), False):
                self.logger.error(bstack11ll1l_opy_ (u"࡚ࠧࡥࡴࡶࠣࡧࡴࡻ࡮ࡵࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠥ৫").format(bstack1lllll1ll_opy_.get(bstack11ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ৬"), bstack11ll1l_opy_ (u"ࠧࡖࡰ࡮ࡲࡴࡽ࡮ࠡࡧࡵࡶࡴࡸࠧ৭"))))
                return 0
            count = bstack1lllll1ll_opy_.get(bstack11ll1l_opy_ (u"ࠨࡥࡲࡹࡳࡺࠧ৮"), 0)
            test_files = bstack1lllll1ll_opy_.get(bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸ࠭৯"), [])
            self.logger.info(bstack11ll1l_opy_ (u"ࠥࡘࡴࡺࡡ࡭ࠢࡷࡩࡸࡺࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧ࠾ࠥࢁࡽࠣৰ").format(count))
            return count
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽࠣৱ").format(e))
            return 0
    def bstack1lll1l1l1_opy_(self, bstack1lllll11l_opy_, bstack111ll11l_opy_):
        bstack111ll11l_opy_[bstack11ll1l_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ৲")] = self.bstack1llll1l1l_opy_
        multiprocessing.set_start_method(bstack11ll1l_opy_ (u"࠭ࡳࡱࡣࡺࡲࠬ৳"))
        bstack1lll1llll_opy_ = []
        manager = multiprocessing.Manager()
        bstack1llll1ll1_opy_ = manager.list()
        if bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৴") in self.bstack1llll1l1l_opy_:
            for index, platform in enumerate(self.bstack1llll1l1l_opy_[bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ৵")]):
                bstack1lll1llll_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1lllll11l_opy_,
                                                            args=(self.bstack11111ll1_opy_, bstack111ll11l_opy_, bstack1llll1ll1_opy_)))
            bstack1llllll1l_opy_ = len(self.bstack1llll1l1l_opy_[bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৶")])
        else:
            bstack1lll1llll_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1lllll11l_opy_,
                                                        args=(self.bstack11111ll1_opy_, bstack111ll11l_opy_, bstack1llll1ll1_opy_)))
            bstack1llllll1l_opy_ = 1
        i = 0
        for t in bstack1lll1llll_opy_:
            os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ৷")] = str(i)
            if bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ৸") in self.bstack1llll1l1l_opy_:
                os.environ[bstack11ll1l_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭৹")] = json.dumps(self.bstack1llll1l1l_opy_[bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৺")][i % bstack1llllll1l_opy_])
            i += 1
            t.start()
        for t in bstack1lll1llll_opy_:
            t.join()
        return list(bstack1llll1ll1_opy_)
    @staticmethod
    def bstack111l1l1l_opy_(driver, bstack1llll111l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ৻"), None)
        if item and getattr(item, bstack11ll1l_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࠪৼ"), None) and not getattr(item, bstack11ll1l_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡳࡵࡥࡤࡰࡰࡨࠫ৽"), False):
            logger.info(
                bstack11ll1l_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠤ৾"))
            bstack1lll1l111_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1lllll1l1_opy_.bstack1lll111ll_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack111l1ll1_opy_(self):
        bstack11ll1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡹࡵࠠࡣࡧࠣࡩࡽ࡫ࡣࡶࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ৿")
        try:
            from browserstack_sdk.bstack11l1lll1_opy_ import bstack11ll1111_opy_
            bstack111lll11_opy_ = bstack11ll1111_opy_(bstack11ll1l11_opy_=self.bstack11111ll1_opy_)
            if not bstack111lll11_opy_.get(bstack11ll1l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭਀"), False):
                self.logger.error(bstack11ll1l_opy_ (u"ࠨࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠥਁ").format(bstack111lll11_opy_.get(bstack11ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ਂ"), bstack11ll1l_opy_ (u"ࠨࡗࡱ࡯ࡳࡵࡷ࡯ࠢࡨࡶࡷࡵࡲࠨਃ"))))
                return []
            test_files = bstack111lll11_opy_.get(bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸ࠭਄"), [])
            count = bstack111lll11_opy_.get(bstack11ll1l_opy_ (u"ࠪࡧࡴࡻ࡮ࡵࠩਅ"), 0)
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸࡪࡪࠠࡼࡿࠣࡸࡪࡹࡴࡴࠢ࡬ࡲࠥࢁࡽࠡࡨ࡬ࡰࡪࡹࠢਆ").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡦࡸࡶ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯࠼ࠣࡿࢂࠨਇ").format(e))
            return []