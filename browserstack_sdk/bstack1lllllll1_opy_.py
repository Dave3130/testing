# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1lll11l11_opy_
from browserstack_sdk.bstack1lll1111l_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1111ll11_opy_
from bstack_utils.bstack1111111l_opy_ import bstack1llllll11_opy_
from bstack_utils.constants import bstack1lllll1ll_opy_
from bstack_utils.bstack1lll1l111_opy_ import bstack111lll11_opy_
class bstack1lll111l1_opy_:
    def __init__(self, args, logger, bstack1111l1ll_opy_, bstack1llll111l_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l1ll_opy_ = bstack1111l1ll_opy_
        self.bstack1llll111l_opy_ = bstack1llll111l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack111l1111_opy_ = []
        self.bstack111ll1ll_opy_ = []
        self.bstack1lll1l1l1_opy_ = []
        self.bstack111ll11l_opy_ = self.bstack111l1l1l_opy_()
        self.bstack1llll11ll_opy_ = -1
    def bstack1lll11l1l_opy_(self, bstack1lll11lll_opy_):
        self.parse_args()
        self.bstack111l11l1_opy_()
        self.bstack1llll1111_opy_(bstack1lll11lll_opy_)
        self.bstack1lll1l1ll_opy_()
    def bstack1lll1ll1l_opy_(self):
        bstack1lll1l111_opy_ = bstack111lll11_opy_.bstack1lll11ll1_opy_(self.bstack1111l1ll_opy_, self.logger)
        if bstack1lll1l111_opy_ is None:
            self.logger.warn(bstack11ll1ll_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡨࡢࡰࡧࡰࡪࡸࠠࡪࡵࠣࡲࡴࡺࠠࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࡨ࠳ࠦࡓ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤ৉"))
            return
        bstack111l1ll1_opy_ = False
        bstack1lll1l111_opy_.bstack1111l11l_opy_(bstack11ll1ll_opy_ (u"ࠢࡦࡰࡤࡦࡱ࡫ࡤࠣ৊"), bstack1lll1l111_opy_.bstack1lll1l11l_opy_())
        start_time = time.time()
        if bstack1lll1l111_opy_.bstack1lll1l11l_opy_():
            test_files = self.bstack1llll1l1l_opy_()
            bstack111l1ll1_opy_ = True
            bstack1111lll1_opy_ = bstack1lll1l111_opy_.bstack1111llll_opy_(test_files)
            if bstack1111lll1_opy_:
                self.bstack111l1111_opy_ = [os.path.normpath(item) for item in bstack1111lll1_opy_]
                self.__111l1l11_opy_()
                bstack1lll1l111_opy_.bstack111111ll_opy_(bstack111l1ll1_opy_)
                self.logger.info(bstack11ll1ll_opy_ (u"ࠣࡖࡨࡷࡹࡹࠠࡳࡧࡲࡶࡩ࡫ࡲࡦࡦࠣࡹࡸ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠼ࠣࡿࢂࠨো").format(self.bstack111l1111_opy_))
            else:
                self.logger.info(bstack11ll1ll_opy_ (u"ࠤࡑࡳࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡺࡩࡷ࡫ࠠࡳࡧࡲࡶࡩ࡫ࡲࡦࡦࠣࡦࡾࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠴ࠢৌ"))
        bstack1lll1l111_opy_.bstack1111l11l_opy_(bstack11ll1ll_opy_ (u"ࠥࡸ࡮ࡳࡥࡕࡣ࡮ࡩࡳ࡚࡯ࡂࡲࡳࡰࡾࠨ্"), int((time.time() - start_time) * 1000)) # bstack1llll1ll1_opy_ to bstack1lllll1l1_opy_
    def __111l1l11_opy_(self):
        bstack11ll1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡴࡱࡧࡣࡦࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࠥࡶࡡࡵࡪࡶࠤ࡮ࡴࠠࡄࡎࡌࠤ࡫ࡲࡡࡨࡵࠣࡻ࡮ࡺࡨࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸࡪࡪࠠࡧ࡫࡯ࡩࠥࡶࡡࡵࡪࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡦࡴࡹࡩࡷࠦࡲࡦࡶࡸࡶࡳࡹࠠࡳࡧࡲࡶࡩ࡫ࡲࡦࡦࠣࡪ࡮ࡲࡥࠡࡰࡤࡱࡪࡹࠬࠡࡣࡱࡨࠥࡽࡥࠡࡵ࡬ࡱࡵࡲࡹࠡࡷࡳࡨࡦࡺࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࡷ࡬ࡪࠦࡃࡍࡋࠣࡥࡷ࡭ࡳࠡࡶࡲࠤࡺࡹࡥࠡࡶ࡫ࡳࡸ࡫ࠠࡧ࡫࡯ࡩࡸ࠴ࠠࡖࡵࡨࡶࠬࡹࠠࡧ࡫࡯ࡸࡪࡸࡩ࡯ࡩࠣࡪࡱࡧࡧࡴࠢࠫ࠱ࡲ࠲ࠠ࠮࡭ࠬࠤࡷ࡫࡭ࡢ࡫ࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡯࡮ࡵࡣࡦࡸࠥࡧ࡮ࡥࠢࡺ࡭ࡱࡲࠠࡣࡧࠣࡥࡵࡶ࡬ࡪࡧࡧࠤࡳࡧࡴࡶࡴࡤࡰࡱࡿࠠࡥࡷࡵ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤৎ")
        try:
            if not self.bstack111l1111_opy_:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡔ࡯ࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡰࡢࡶ࡫ࠤࡹࡵࠠࡴࡧࡷࠦ৏"))
                return
            bstack111l111l_opy_ = []
            for flag in self.bstack111ll1ll_opy_:
                if flag.startswith(bstack11ll1ll_opy_ (u"࠭࠭ࠨ৐")):
                    bstack111l111l_opy_.append(flag)
                    continue
                bstack1llll11l1_opy_ = False
                if bstack11ll1ll_opy_ (u"ࠧ࠻࠼ࠪ৑") in flag:
                    bstack11111ll1_opy_ = flag.split(bstack11ll1ll_opy_ (u"ࠨ࠼࠽ࠫ৒"), 1)[0]
                    if os.path.exists(bstack11111ll1_opy_):
                        bstack1llll11l1_opy_ = True
                elif os.path.exists(flag):
                    if os.path.isdir(flag) or (os.path.isfile(flag) and flag.endswith(bstack11ll1ll_opy_ (u"ࠩ࠱ࡴࡾ࠭৓"))):
                        bstack1llll11l1_opy_ = True
                if not bstack1llll11l1_opy_:
                    bstack111l111l_opy_.append(flag)
            bstack111l111l_opy_.extend(self.bstack111l1111_opy_)
            self.bstack111ll1ll_opy_ = bstack111l111l_opy_
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶࡨࡨࠥࡹࡥ࡭ࡧࡦࡸࡴࡸࡳ࠻ࠢࡾࢁࠧ৔").format(str(e)))
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1lll111ll_opy_():
        import importlib
        if getattr(importlib, bstack11ll1ll_opy_ (u"ࠫ࡫࡯࡮ࡥࡡ࡯ࡳࡦࡪࡥࡳࠩ৕"), False):
            bstack111l1lll_opy_ = importlib.find_loader(bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ৖"))
        else:
            bstack111l1lll_opy_ = importlib.util.find_spec(bstack11ll1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨৗ"))
    def bstack1111ll1l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1llll11ll_opy_ = -1
        if self.bstack1llll111l_opy_ and bstack11ll1ll_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ৘") in self.bstack1111l1ll_opy_:
            self.bstack1llll11ll_opy_ = int(self.bstack1111l1ll_opy_[bstack11ll1ll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ৙")])
        try:
            bstack1lll1lll1_opy_ = [bstack11ll1ll_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫ৚"), bstack11ll1ll_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭৛"), bstack11ll1ll_opy_ (u"ࠫ࠲ࡶࠧড়")]
            if self.bstack1llll11ll_opy_ >= 0:
                bstack1lll1lll1_opy_.extend([bstack11ll1ll_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ঢ়"), bstack11ll1ll_opy_ (u"࠭࠭࡯ࠩ৞")])
            for arg in bstack1lll1lll1_opy_:
                self.bstack1111ll1l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111l11l1_opy_(self):
        bstack111ll1ll_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack111ll1ll_opy_ = bstack111ll1ll_opy_
        return self.bstack111ll1ll_opy_
    def bstack1lll1ll11_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1lll111ll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1111ll11_opy_)
    def bstack1llll1111_opy_(self, bstack1lll11lll_opy_):
        bstack1llllll1l_opy_ = Config.bstack1lll11ll1_opy_()
        if bstack1lll11lll_opy_:
            self.bstack111ll1ll_opy_.append(bstack11ll1ll_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫয়"))
            self.bstack111ll1ll_opy_.append(bstack11ll1ll_opy_ (u"ࠨࡖࡵࡹࡪ࠭ৠ"))
        if bstack1llllll1l_opy_.bstack111111l1_opy_():
            self.bstack111ll1ll_opy_.append(bstack11ll1ll_opy_ (u"ࠩ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨৡ"))
            self.bstack111ll1ll_opy_.append(bstack11ll1ll_opy_ (u"ࠪࡘࡷࡻࡥࠨৢ"))
        self.bstack111ll1ll_opy_.append(bstack11ll1ll_opy_ (u"ࠫ࠲ࡶࠧৣ"))
        self.bstack111ll1ll_opy_.append(bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠪ৤"))
        self.bstack111ll1ll_opy_.append(bstack11ll1ll_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨ৥"))
        self.bstack111ll1ll_opy_.append(bstack11ll1ll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ০"))
        if self.bstack1llll11ll_opy_ > 1:
            self.bstack111ll1ll_opy_.append(bstack11ll1ll_opy_ (u"ࠨ࠯ࡱࠫ১"))
            self.bstack111ll1ll_opy_.append(str(self.bstack1llll11ll_opy_))
    def bstack1lll1l1ll_opy_(self):
        if bstack1llllll11_opy_.bstack1lll1llll_opy_(self.bstack1111l1ll_opy_):
             self.bstack111ll1ll_opy_ += [
                bstack1lllll1ll_opy_.get(bstack11ll1ll_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࠨ২")), str(bstack1llllll11_opy_.bstack111l11ll_opy_(self.bstack1111l1ll_opy_)),
                bstack1lllll1ll_opy_.get(bstack11ll1ll_opy_ (u"ࠪࡨࡪࡲࡡࡺࠩ৩")), str(bstack1lllll1ll_opy_.get(bstack11ll1ll_opy_ (u"ࠫࡷ࡫ࡲࡶࡰ࠰ࡨࡪࡲࡡࡺࠩ৪")))
            ]
    def bstack11111111_opy_(self):
        bstack1lll1l1l1_opy_ = []
        for spec in self.bstack111l1111_opy_:
            bstack1lllll11l_opy_ = [spec]
            bstack1lllll11l_opy_ += self.bstack111ll1ll_opy_
            bstack1lll1l1l1_opy_.append(bstack1lllll11l_opy_)
        self.bstack1lll1l1l1_opy_ = bstack1lll1l1l1_opy_
        return bstack1lll1l1l1_opy_
    def bstack111l1l1l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111ll11l_opy_ = True
            return True
        except Exception as e:
            self.bstack111ll11l_opy_ = False
        return self.bstack111ll11l_opy_
    def bstack1llllllll_opy_(self):
        bstack11ll1ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡊࡩࡹࠦࡴࡩࡧࠣࡧࡴࡻ࡮ࡵࠢࡲࡪࠥࡺࡥࡴࡶࡶࠤࡼ࡯ࡴࡩࡱࡸࡸࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡴࡩࡧࡰࠤࡺࡹࡩ࡯ࡩࠣࡴࡾࡺࡥࡴࡶࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࡹࡀࠠࡕࡪࡨࠤࡹࡵࡴࡢ࡮ࠣࡲࡺࡳࡢࡦࡴࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ৫")
        try:
            from browserstack_sdk.bstack11l1ll1l_opy_ import bstack11ll1l1l_opy_
            bstack1111l111_opy_ = bstack11ll1l1l_opy_(bstack11l1lll1_opy_=self.bstack111ll1ll_opy_)
            if not bstack1111l111_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ৬"), False):
                self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡕࡧࡶࡸࠥࡩ࡯ࡶࡰࡷࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢࡾࢁࠧ৭").format(bstack1111l111_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ৮"), bstack11ll1ll_opy_ (u"ࠩࡘࡲࡰࡴ࡯ࡸࡰࠣࡩࡷࡸ࡯ࡳࠩ৯"))))
                return 0
            count = bstack1111l111_opy_.get(bstack11ll1ll_opy_ (u"ࠪࡧࡴࡻ࡮ࡵࠩৰ"), 0)
            self.logger.info(bstack11ll1ll_opy_ (u"࡙ࠦࡵࡴࡢ࡮ࠣࡸࡪࡹࡴࡴࠢࡦࡳࡱࡲࡥࡤࡶࡨࡨ࠿ࠦࡻࡾࠤৱ").format(count))
            return count
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡰࡷࡱࡸ࠿ࠦࡻࡾࠤ৲").format(e))
            return 0
    def bstack1lllll111_opy_(self, bstack11111l1l_opy_, bstack1lll11l1l_opy_):
        bstack1lll11l1l_opy_[bstack11ll1ll_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭৳")] = self.bstack1111l1ll_opy_
        multiprocessing.set_start_method(bstack11ll1ll_opy_ (u"ࠧࡴࡲࡤࡻࡳ࠭৴"))
        bstack11111l11_opy_ = []
        manager = multiprocessing.Manager()
        bstack1llll1lll_opy_ = manager.list()
        if bstack11ll1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ৵") in self.bstack1111l1ll_opy_:
            for index, platform in enumerate(self.bstack1111l1ll_opy_[bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৶")]):
                bstack11111l11_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11111l1l_opy_,
                                                            args=(self.bstack111ll1ll_opy_, bstack1lll11l1l_opy_, bstack1llll1lll_opy_)))
            bstack1111l1l1_opy_ = len(self.bstack1111l1ll_opy_[bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৷")])
        else:
            bstack11111l11_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11111l1l_opy_,
                                                        args=(self.bstack111ll1ll_opy_, bstack1lll11l1l_opy_, bstack1llll1lll_opy_)))
            bstack1111l1l1_opy_ = 1
        i = 0
        for t in bstack11111l11_opy_:
            os.environ[bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ৸")] = str(i)
            if bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৹") in self.bstack1111l1ll_opy_:
                os.environ[bstack11ll1ll_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧ৺")] = json.dumps(self.bstack1111l1ll_opy_[bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৻")][i % bstack1111l1l1_opy_])
            i += 1
            t.start()
        for t in bstack11111l11_opy_:
            t.join()
        return list(bstack1llll1lll_opy_)
    @staticmethod
    def bstack11111lll_opy_(driver, bstack1llll1l11_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬৼ"), None)
        if item and getattr(item, bstack11ll1ll_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡣࡢࡵࡨࠫ৽"), None) and not getattr(item, bstack11ll1ll_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡶࡸࡴࡶ࡟ࡥࡱࡱࡩࠬ৾"), False):
            logger.info(
                bstack11ll1ll_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠢࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡮ࡹࠠࡶࡰࡧࡩࡷࡽࡡࡺ࠰ࠥ৿"))
            bstack111lll1l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1lll11l11_opy_.bstack111ll1l1_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1llll1l1l_opy_(self):
        bstack11ll1ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠ࡭࡫ࡶࡸࠥࡵࡦࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡺ࡯ࠡࡤࡨࠤࡪࡾࡥࡤࡷࡷࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ਀")
        try:
            from browserstack_sdk.bstack11l1ll1l_opy_ import bstack11ll1l1l_opy_
            bstack111ll111_opy_ = bstack11ll1l1l_opy_(bstack11l1lll1_opy_=self.bstack111ll1ll_opy_)
            if not bstack111ll111_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧਁ"), False):
                self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡕࡧࡶࡸࠥ࡬ࡩ࡭ࡧࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪ࠺ࠡࡽࢀࠦਂ").format(bstack111ll111_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧਃ"), bstack11ll1ll_opy_ (u"ࠩࡘࡲࡰࡴ࡯ࡸࡰࠣࡩࡷࡸ࡯ࡳࠩ਄"))))
                return []
            test_files = bstack111ll111_opy_.get(bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹࠧਅ"), [])
            count = bstack111ll111_opy_.get(bstack11ll1ll_opy_ (u"ࠫࡨࡵࡵ࡯ࡶࠪਆ"), 0)
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡉ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠡࡽࢀࠤࡹ࡫ࡳࡵࡵࠣ࡭ࡳࠦࡻࡾࠢࡩ࡭ࡱ࡫ࡳࠣਇ").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡧࡹࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰ࠽ࠤࢀࢃࠢਈ").format(e))
            return []