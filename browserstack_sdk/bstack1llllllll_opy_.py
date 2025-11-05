# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack111ll1ll_opy_
from browserstack_sdk.bstack1llllll1l_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1llll11ll_opy_
from bstack_utils.bstack1lll1l11l_opy_ import bstack111l1l1l_opy_
from bstack_utils.constants import bstack1lll11ll1_opy_
from bstack_utils.bstack1lll1llll_opy_ import bstack1lll1ll11_opy_
class bstack1111l111_opy_:
    def __init__(self, args, logger, bstack1lll11l1l_opy_, bstack1lll1l1ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll11l1l_opy_ = bstack1lll11l1l_opy_
        self.bstack1lll1l1ll_opy_ = bstack1lll1l1ll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1llll111l_opy_ = []
        self.bstack11l1111l_opy_ = []
        self.bstack111l111l_opy_ = []
        self.bstack111l11l1_opy_ = self.bstack1llll1l11_opy_()
        self.bstack1111ll1l_opy_ = -1
    def bstack1lllll1ll_opy_(self, bstack1llll1ll1_opy_):
        self.parse_args()
        self.bstack1llll1111_opy_()
        self.bstack111111ll_opy_(bstack1llll1ll1_opy_)
        self.bstack111111l1_opy_()
    def bstack1111l1ll_opy_(self):
        bstack1lll1llll_opy_ = bstack1lll1ll11_opy_.bstack111l1111_opy_(self.bstack1lll11l1l_opy_, self.logger)
        if bstack1lll1llll_opy_ is None:
            self.logger.warn(bstack1lll11l_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡩࡣࡱࡨࡱ࡫ࡲࠡ࡫ࡶࠤࡳࡵࡴࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡩ࠴ࠠࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥম"))
            return
        bstack11111111_opy_ = False
        bstack1lll1llll_opy_.bstack1lllll11l_opy_(bstack1lll11l_opy_ (u"ࠣࡧࡱࡥࡧࡲࡥࡥࠤয"), bstack1lll1llll_opy_.bstack1111llll_opy_())
        start_time = time.time()
        if bstack1lll1llll_opy_.bstack1111llll_opy_():
            test_files = self.bstack1111ll11_opy_()
            bstack11111111_opy_ = True
            bstack1lll1l1l1_opy_ = bstack1lll1llll_opy_.bstack1lllll111_opy_(test_files)
            if bstack1lll1l1l1_opy_:
                self.bstack1llll111l_opy_ = [os.path.normpath(item) for item in bstack1lll1l1l1_opy_]
                self.__111lll1l_opy_()
                bstack1lll1llll_opy_.bstack11l11111_opy_(bstack11111111_opy_)
                self.logger.info(bstack1lll11l_opy_ (u"ࠤࡗࡩࡸࡺࡳࠡࡴࡨࡳࡷࡪࡥࡳࡧࡧࠤࡺࡹࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠽ࠤࢀࢃࠢর").format(self.bstack1llll111l_opy_))
            else:
                self.logger.info(bstack1lll11l_opy_ (u"ࠥࡒࡴࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡻࡪࡸࡥࠡࡴࡨࡳࡷࡪࡥࡳࡧࡧࠤࡧࡿࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣ঱"))
        bstack1lll1llll_opy_.bstack1lllll11l_opy_(bstack1lll11l_opy_ (u"ࠦࡹ࡯࡭ࡦࡖࡤ࡯ࡪࡴࡔࡰࡃࡳࡴࡱࡿࠢল"), int((time.time() - start_time) * 1000)) # bstack111ll11l_opy_ to bstack1lll11lll_opy_
    def __111lll1l_opy_(self):
        bstack1lll11l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡵࡲࡡࡤࡧࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࠦࡰࡢࡶ࡫ࡷࠥ࡯࡮ࠡࡅࡏࡍࠥ࡬࡬ࡢࡩࡶࠤࡼ࡯ࡴࡩࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡫ࡤࠡࡨ࡬ࡰࡪࠦࡰࡢࡶ࡫ࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡴࡧࡵࡺࡪࡸࠠࡳࡧࡷࡹࡷࡴࡳࠡࡴࡨࡳࡷࡪࡥࡳࡧࡧࠤ࡫࡯࡬ࡦࠢࡱࡥࡲ࡫ࡳ࠭ࠢࡤࡲࡩࠦࡷࡦࠢࡶ࡭ࡲࡶ࡬ࡺࠢࡸࡴࡩࡧࡴࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࡸ࡭࡫ࠠࡄࡎࡌࠤࡦࡸࡧࡴࠢࡷࡳࠥࡻࡳࡦࠢࡷ࡬ࡴࡹࡥࠡࡨ࡬ࡰࡪࡹ࠮ࠡࡗࡶࡩࡷ࠭ࡳࠡࡨ࡬ࡰࡹ࡫ࡲࡪࡰࡪࠤ࡫ࡲࡡࡨࡵࠣࠬ࠲ࡳࠬࠡ࠯࡮࠭ࠥࡸࡥ࡮ࡣ࡬ࡲࠏࠦࠠࠡࠢࠣࠤࠥࠦࡩ࡯ࡶࡤࡧࡹࠦࡡ࡯ࡦࠣࡻ࡮ࡲ࡬ࠡࡤࡨࠤࡦࡶࡰ࡭࡫ࡨࡨࠥࡴࡡࡵࡷࡵࡥࡱࡲࡹࠡࡦࡸࡶ࡮ࡴࡧࠡࡲࡼࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ঳")
        try:
            if not self.bstack1llll111l_opy_:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡎࡰࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡫ࡤࠡࡨ࡬ࡰࡪࡹࠠࡱࡣࡷ࡬ࠥࡺ࡯ࠡࡵࡨࡸࠧ঴"))
                return
            bstack1llll1lll_opy_ = []
            for flag in self.bstack11l1111l_opy_:
                if flag.startswith(bstack1lll11l_opy_ (u"ࠧ࠮ࠩ঵")):
                    bstack1llll1lll_opy_.append(flag)
                    continue
                bstack11111l1l_opy_ = False
                if bstack1lll11l_opy_ (u"ࠨ࠼࠽ࠫশ") in flag:
                    bstack1llll11l1_opy_ = flag.split(bstack1lll11l_opy_ (u"ࠩ࠽࠾ࠬষ"), 1)[0]
                    if os.path.exists(bstack1llll11l1_opy_):
                        bstack11111l1l_opy_ = True
                elif os.path.exists(flag):
                    if os.path.isdir(flag) or (os.path.isfile(flag) and flag.endswith(bstack1lll11l_opy_ (u"ࠪ࠲ࡵࡿࠧস"))):
                        bstack11111l1l_opy_ = True
                if not bstack11111l1l_opy_:
                    bstack1llll1lll_opy_.append(flag)
            bstack1llll1lll_opy_.extend(self.bstack1llll111l_opy_)
            self.bstack11l1111l_opy_ = bstack1llll1lll_opy_
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷࡩࡩࠦࡳࡦ࡮ࡨࡧࡹࡵࡲࡴ࠼ࠣࡿࢂࠨহ").format(str(e)))
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1lll1lll1_opy_():
        import importlib
        if getattr(importlib, bstack1lll11l_opy_ (u"ࠬ࡬ࡩ࡯ࡦࡢࡰࡴࡧࡤࡦࡴࠪ঺"), False):
            bstack111l1l11_opy_ = importlib.find_loader(bstack1lll11l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨ঻"))
        else:
            bstack111l1l11_opy_ = importlib.util.find_spec(bstack1lll11l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮়ࠩ"))
    def bstack11111l11_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1111ll1l_opy_ = -1
        if self.bstack1lll1l1ll_opy_ and bstack1lll11l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨঽ") in self.bstack1lll11l1l_opy_:
            self.bstack1111ll1l_opy_ = int(self.bstack1lll11l1l_opy_[bstack1lll11l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩা")])
        try:
            bstack1111lll1_opy_ = [bstack1lll11l_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶࠬি"), bstack1lll11l_opy_ (u"ࠫ࠲࠳ࡰ࡭ࡷࡪ࡭ࡳࡹࠧী"), bstack1lll11l_opy_ (u"ࠬ࠳ࡰࠨু")]
            if self.bstack1111ll1l_opy_ >= 0:
                bstack1111lll1_opy_.extend([bstack1lll11l_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧূ"), bstack1lll11l_opy_ (u"ࠧ࠮ࡰࠪৃ")])
            for arg in bstack1111lll1_opy_:
                self.bstack11111l11_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1llll1111_opy_(self):
        bstack11l1111l_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11l1111l_opy_ = bstack11l1111l_opy_
        return self.bstack11l1111l_opy_
    def bstack111llll1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1lll1lll1_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1llll11ll_opy_)
    def bstack111111ll_opy_(self, bstack1llll1ll1_opy_):
        bstack111ll1l1_opy_ = Config.bstack111l1111_opy_()
        if bstack1llll1ll1_opy_:
            self.bstack11l1111l_opy_.append(bstack1lll11l_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬৄ"))
            self.bstack11l1111l_opy_.append(bstack1lll11l_opy_ (u"ࠩࡗࡶࡺ࡫ࠧ৅"))
        if bstack111ll1l1_opy_.bstack1llll1l1l_opy_():
            self.bstack11l1111l_opy_.append(bstack1lll11l_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ৆"))
            self.bstack11l1111l_opy_.append(bstack1lll11l_opy_ (u"࡙ࠫࡸࡵࡦࠩে"))
        self.bstack11l1111l_opy_.append(bstack1lll11l_opy_ (u"ࠬ࠳ࡰࠨৈ"))
        self.bstack11l1111l_opy_.append(bstack1lll11l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠫ৉"))
        self.bstack11l1111l_opy_.append(bstack1lll11l_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩ৊"))
        self.bstack11l1111l_opy_.append(bstack1lll11l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨো"))
        if self.bstack1111ll1l_opy_ > 1:
            self.bstack11l1111l_opy_.append(bstack1lll11l_opy_ (u"ࠩ࠰ࡲࠬৌ"))
            self.bstack11l1111l_opy_.append(str(self.bstack1111ll1l_opy_))
    def bstack111111l1_opy_(self):
        if bstack111l1l1l_opy_.bstack11111lll_opy_(self.bstack1lll11l1l_opy_):
             self.bstack11l1111l_opy_ += [
                bstack1lll11ll1_opy_.get(bstack1lll11l_opy_ (u"ࠪࡶࡪࡸࡵ࡯্ࠩ")), str(bstack111l1l1l_opy_.bstack111l11ll_opy_(self.bstack1lll11l1l_opy_)),
                bstack1lll11ll1_opy_.get(bstack1lll11l_opy_ (u"ࠫࡩ࡫࡬ࡢࡻࠪৎ")), str(bstack1lll11ll1_opy_.get(bstack1lll11l_opy_ (u"ࠬࡸࡥࡳࡷࡱ࠱ࡩ࡫࡬ࡢࡻࠪ৏")))
            ]
    def bstack1lllll1l1_opy_(self):
        bstack111l111l_opy_ = []
        for spec in self.bstack1llll111l_opy_:
            bstack111l1lll_opy_ = [spec]
            bstack111l1lll_opy_ += self.bstack11l1111l_opy_
            bstack111l111l_opy_.append(bstack111l1lll_opy_)
        self.bstack111l111l_opy_ = bstack111l111l_opy_
        return bstack111l111l_opy_
    def bstack1llll1l11_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111l11l1_opy_ = True
            return True
        except Exception as e:
            self.bstack111l11l1_opy_ = False
        return self.bstack111l11l1_opy_
    def bstack1111111l_opy_(self):
        bstack1lll11l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡋࡪࡺࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥࡽࡩࡵࡪࡲࡹࡹࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡵࡪࡨࡱࠥࡻࡳࡪࡰࡪࠤࡵࡿࡴࡦࡵࡷࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡭ࡳࡺ࠺ࠡࡖ࡫ࡩࠥࡺ࡯ࡵࡣ࡯ࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࡣࡰ࡮࡯ࡩࡨࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ৐")
        try:
            from browserstack_sdk.bstack11ll111l_opy_ import bstack11ll1l1l_opy_
            bstack1lllllll1_opy_ = bstack11ll1l1l_opy_(bstack11ll11ll_opy_=self.bstack11l1111l_opy_)
            if not bstack1lllllll1_opy_.get(bstack1lll11l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ৑"), False):
                self.logger.error(bstack1lll11l_opy_ (u"ࠣࡖࡨࡷࡹࠦࡣࡰࡷࡱࡸࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡿࢂࠨ৒").format(bstack1lllllll1_opy_.get(bstack1lll11l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ৓"), bstack1lll11l_opy_ (u"࡙ࠪࡳࡱ࡮ࡰࡹࡱࠤࡪࡸࡲࡰࡴࠪ৔"))))
                return 0
            count = bstack1lllllll1_opy_.get(bstack1lll11l_opy_ (u"ࠫࡨࡵࡵ࡯ࡶࠪ৕"), 0)
            self.logger.info(bstack1lll11l_opy_ (u"࡚ࠧ࡯ࡵࡣ࡯ࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࡀࠠࡼࡿࠥ৖").format(count))
            return count
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡱࡸࡲࡹࡀࠠࡼࡿࠥৗ").format(e))
            return 0
    def bstack1llllll11_opy_(self, bstack1lll1ll1l_opy_, bstack1lllll1ll_opy_):
        bstack1lllll1ll_opy_[bstack1lll11l_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧ৘")] = self.bstack1lll11l1l_opy_
        multiprocessing.set_start_method(bstack1lll11l_opy_ (u"ࠨࡵࡳࡥࡼࡴࠧ৙"))
        bstack111ll111_opy_ = []
        manager = multiprocessing.Manager()
        bstack11111ll1_opy_ = manager.list()
        if bstack1lll11l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৚") in self.bstack1lll11l1l_opy_:
            for index, platform in enumerate(self.bstack1lll11l1l_opy_[bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৛")]):
                bstack111ll111_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1lll1ll1l_opy_,
                                                            args=(self.bstack11l1111l_opy_, bstack1lllll1ll_opy_, bstack11111ll1_opy_)))
            bstack1111l11l_opy_ = len(self.bstack1lll11l1l_opy_[bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧড়")])
        else:
            bstack111ll111_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1lll1ll1l_opy_,
                                                        args=(self.bstack11l1111l_opy_, bstack1lllll1ll_opy_, bstack11111ll1_opy_)))
            bstack1111l11l_opy_ = 1
        i = 0
        for t in bstack111ll111_opy_:
            os.environ[bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬঢ়")] = str(i)
            if bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৞") in self.bstack1lll11l1l_opy_:
                os.environ[bstack1lll11l_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨয়")] = json.dumps(self.bstack1lll11l1l_opy_[bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫৠ")][i % bstack1111l11l_opy_])
            i += 1
            t.start()
        for t in bstack111ll111_opy_:
            t.join()
        return list(bstack11111ll1_opy_)
    @staticmethod
    def bstack1lll1l111_opy_(driver, bstack1111l1l1_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1lll11l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ৡ"), None)
        if item and getattr(item, bstack1lll11l_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡤࡣࡶࡩࠬৢ"), None) and not getattr(item, bstack1lll11l_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࡠࡦࡲࡲࡪ࠭ৣ"), False):
            logger.info(
                bstack1lll11l_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠣࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡷࡱࡨࡪࡸࡷࡢࡻ࠱ࠦ৤"))
            bstack111l1ll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack111ll1ll_opy_.bstack111lll11_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1111ll11_opy_(self):
        bstack1lll11l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶࠤࡹ࡮ࡥࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡴࡰࠢࡥࡩࠥ࡫ࡸࡦࡥࡸࡸࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ৥")
        try:
            from browserstack_sdk.bstack11ll111l_opy_ import bstack11ll1l1l_opy_
            bstack111lllll_opy_ = bstack11ll1l1l_opy_(bstack11ll11ll_opy_=self.bstack11l1111l_opy_)
            if not bstack111lllll_opy_.get(bstack1lll11l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ০"), False):
                self.logger.error(bstack1lll11l_opy_ (u"ࠣࡖࡨࡷࡹࠦࡦࡪ࡮ࡨࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢࡾࢁࠧ১").format(bstack111lllll_opy_.get(bstack1lll11l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ২"), bstack1lll11l_opy_ (u"࡙ࠪࡳࡱ࡮ࡰࡹࡱࠤࡪࡸࡲࡰࡴࠪ৩"))))
                return []
            test_files = bstack111lllll_opy_.get(bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳࠨ৪"), [])
            count = bstack111lllll_opy_.get(bstack1lll11l_opy_ (u"ࠬࡩ࡯ࡶࡰࡷࠫ৫"), 0)
            self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡃࡰ࡮࡯ࡩࡨࡺࡥࡥࠢࡾࢁࠥࡺࡥࡴࡶࡶࠤ࡮ࡴࠠࡼࡿࠣࡪ࡮ࡲࡥࡴࠤ৬").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡨࡺࡸࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠾ࠥࢁࡽࠣ৭").format(e))
            return []