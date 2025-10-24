# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack11l1111l_opy_
from browserstack_sdk.bstack1111111l_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1llll1l11_opy_
from bstack_utils.bstack1111ll11_opy_ import bstack111lll1l_opy_
from bstack_utils.constants import bstack1111llll_opy_
from bstack_utils.bstack1llllll11_opy_ import bstack1llll111l_opy_
class bstack111111ll_opy_:
    def __init__(self, args, logger, bstack11111l11_opy_, bstack1111l11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack11111l11_opy_ = bstack11111l11_opy_
        self.bstack1111l11l_opy_ = bstack1111l11l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1lll1ll1l_opy_ = []
        self.bstack1lll11lll_opy_ = []
        self.bstack1lll1l1l1_opy_ = []
        self.bstack111l1ll1_opy_ = self.bstack1lll1lll1_opy_()
        self.bstack111l111l_opy_ = -1
    def bstack1llllll1l_opy_(self, bstack11111111_opy_):
        self.parse_args()
        self.bstack111l1l1l_opy_()
        self.bstack111lll11_opy_(bstack11111111_opy_)
        self.bstack1lllll111_opy_()
    def bstack111l11ll_opy_(self):
        bstack1llllll11_opy_ = bstack1llll111l_opy_.bstack1111ll1l_opy_(self.bstack11111l11_opy_, self.logger)
        if bstack1llllll11_opy_ is None:
            self.logger.warn(bstack1l1_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡲࡩࡲࡥࡳࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦয"))
            return
        bstack1llll1lll_opy_ = False
        bstack1llllll11_opy_.bstack1lllll1l1_opy_(bstack1l1_opy_ (u"ࠤࡨࡲࡦࡨ࡬ࡦࡦࠥর"), bstack1llllll11_opy_.bstack1lll1llll_opy_())
        start_time = time.time()
        if bstack1llllll11_opy_.bstack1lll1llll_opy_():
            test_files = self.bstack11111l1l_opy_()
            bstack1llll1lll_opy_ = True
            bstack111ll1ll_opy_ = bstack1llllll11_opy_.bstack111ll111_opy_(test_files)
            if bstack111ll1ll_opy_:
                self.bstack1lll1ll1l_opy_ = [os.path.normpath(item).replace(bstack1l1_opy_ (u"ࠪࡠࡡ࠭঱"), bstack1l1_opy_ (u"ࠫ࠴࠭ল")) for item in bstack111ll1ll_opy_]
                self.__1111l1ll_opy_()
                bstack1llllll11_opy_.bstack1lll1l111_opy_(bstack1llll1lll_opy_)
                self.logger.info(bstack1l1_opy_ (u"࡚ࠧࡥࡴࡶࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡶࡵ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥ঳").format(self.bstack1lll1ll1l_opy_))
            else:
                self.logger.info(bstack1l1_opy_ (u"ࠨࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡦࡴࡨࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡣࡻࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦ঴"))
        bstack1llllll11_opy_.bstack1lllll1l1_opy_(bstack1l1_opy_ (u"ࠢࡵ࡫ࡰࡩ࡙ࡧ࡫ࡦࡰࡗࡳࡆࡶࡰ࡭ࡻࠥ঵"), int((time.time() - start_time) * 1000)) # bstack1llll11l1_opy_ to bstack1111l111_opy_
    def __1111l1ll_opy_(self):
        bstack1l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡱ࡮ࡤࡧࡪࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࠢࡳࡥࡹ࡮ࡳࠡ࡫ࡱࠤࡈࡒࡉࠡࡨ࡯ࡥ࡬ࡹࠠࡸ࡫ࡷ࡬ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵࡧࡧࠤ࡫࡯࡬ࡦࠢࡳࡥࡹ࡮ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡪࡸࡶࡦࡴࠣࡶࡪࡺࡵࡳࡰࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡧ࡫࡯ࡩࠥࡴࡡ࡮ࡧࡶ࠰ࠥࡧ࡮ࡥࠢࡺࡩࠥࡹࡩ࡮ࡲ࡯ࡽࠥࡻࡰࡥࡣࡷࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࡴࡩࡧࠣࡇࡑࡏࠠࡢࡴࡪࡷࠥࡺ࡯ࠡࡷࡶࡩࠥࡺࡨࡰࡵࡨࠤ࡫࡯࡬ࡦࡵ࠱ࠤ࡚ࡹࡥࡳࠩࡶࠤ࡫࡯࡬ࡵࡧࡵ࡭ࡳ࡭ࠠࡧ࡮ࡤ࡫ࡸࠦࠨ࠮࡯࠯ࠤ࠲ࡱࠩࠡࡴࡨࡱࡦ࡯࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࡹࡧࡣࡵࠢࡤࡲࡩࠦࡷࡪ࡮࡯ࠤࡧ࡫ࠠࡢࡲࡳࡰ࡮࡫ࡤࠡࡰࡤࡸࡺࡸࡡ࡭࡮ࡼࠤࡩࡻࡲࡪࡰࡪࠤࡵࡿࡴࡦࡵࡷࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨশ")
        try:
            if not self.bstack1lll1ll1l_opy_:
                self.logger.debug(bstack1l1_opy_ (u"ࠤࡑࡳࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡴࡦࡺࡨࠡࡶࡲࠤࡸ࡫ࡴࠣষ"))
                return
            bstack1llll1ll1_opy_ = []
            bstack11111lll_opy_ = []
            for flag in self.bstack1lll11lll_opy_:
                if flag.startswith(bstack1l1_opy_ (u"ࠪ࠱ࠬস")):
                    bstack1llll1ll1_opy_.append(flag)
                    continue
                bstack111llll1_opy_ = False
                if bstack1l1_opy_ (u"ࠫ࠿ࡀࠧহ") in flag:
                    bstack111llll1_opy_ = True
                elif flag.endswith(bstack1l1_opy_ (u"ࠬ࠴ࡰࡺࠩ঺")):
                    bstack111llll1_opy_ = True
                elif os.path.exists(flag):
                    if os.path.isdir(flag) or (os.path.isfile(flag) and flag.endswith(bstack1l1_opy_ (u"࠭࠮ࡱࡻࠪ঻"))):
                        bstack111llll1_opy_ = True
                if not bstack111llll1_opy_:
                    bstack1llll1ll1_opy_.append(flag)
                else:
                    bstack11111lll_opy_.append(flag)
            bstack1llll1ll1_opy_.extend(self.bstack1lll1ll1l_opy_)
            self.bstack1lll11lll_opy_ = bstack1llll1ll1_opy_
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡥࡥࠢࡶࡩࡱ࡫ࡣࡵࡱࡵࡷ࠿ࠦࡻࡾࠤ়").format(str(e)))
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1llll1111_opy_():
        import importlib
        if getattr(importlib, bstack1l1_opy_ (u"ࠨࡨ࡬ࡲࡩࡥ࡬ࡰࡣࡧࡩࡷ࠭ঽ"), False):
            bstack111l11l1_opy_ = importlib.find_loader(bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫা"))
        else:
            bstack111l11l1_opy_ = importlib.util.find_spec(bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬি"))
    def bstack111lllll_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack111l111l_opy_ = -1
        if self.bstack1111l11l_opy_ and bstack1l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫী") in self.bstack11111l11_opy_:
            self.bstack111l111l_opy_ = int(self.bstack11111l11_opy_[bstack1l1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬু")])
        try:
            bstack1111lll1_opy_ = [bstack1l1_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨূ"), bstack1l1_opy_ (u"ࠧ࠮࠯ࡳࡰࡺ࡭ࡩ࡯ࡵࠪৃ"), bstack1l1_opy_ (u"ࠨ࠯ࡳࠫৄ")]
            if self.bstack111l111l_opy_ >= 0:
                bstack1111lll1_opy_.extend([bstack1l1_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ৅"), bstack1l1_opy_ (u"ࠪ࠱ࡳ࠭৆")])
            for arg in bstack1111lll1_opy_:
                self.bstack111lllll_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111l1l1l_opy_(self):
        bstack1lll11lll_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1lll11lll_opy_ = bstack1lll11lll_opy_
        return self.bstack1lll11lll_opy_
    def bstack1lllll1ll_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1llll1111_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1llll1l11_opy_)
    def bstack111lll11_opy_(self, bstack11111111_opy_):
        bstack11l11111_opy_ = Config.bstack1111ll1l_opy_()
        if bstack11111111_opy_:
            self.bstack1lll11lll_opy_.append(bstack1l1_opy_ (u"ࠫ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨে"))
            self.bstack1lll11lll_opy_.append(bstack1l1_opy_ (u"࡚ࠬࡲࡶࡧࠪৈ"))
        if bstack11l11111_opy_.bstack1lll11l1l_opy_():
            self.bstack1lll11lll_opy_.append(bstack1l1_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬ৉"))
            self.bstack1lll11lll_opy_.append(bstack1l1_opy_ (u"ࠧࡕࡴࡸࡩࠬ৊"))
        self.bstack1lll11lll_opy_.append(bstack1l1_opy_ (u"ࠨ࠯ࡳࠫো"))
        self.bstack1lll11lll_opy_.append(bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠧৌ"))
        self.bstack1lll11lll_opy_.append(bstack1l1_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶ্ࠬ"))
        self.bstack1lll11lll_opy_.append(bstack1l1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫৎ"))
        if self.bstack111l111l_opy_ > 1:
            self.bstack1lll11lll_opy_.append(bstack1l1_opy_ (u"ࠬ࠳࡮ࠨ৏"))
            self.bstack1lll11lll_opy_.append(str(self.bstack111l111l_opy_))
    def bstack1lllll111_opy_(self):
        if bstack111lll1l_opy_.bstack1lll1l11l_opy_(self.bstack11111l11_opy_):
             self.bstack1lll11lll_opy_ += [
                bstack1111llll_opy_.get(bstack1l1_opy_ (u"࠭ࡲࡦࡴࡸࡲࠬ৐")), str(bstack111lll1l_opy_.bstack111l1l11_opy_(self.bstack11111l11_opy_)),
                bstack1111llll_opy_.get(bstack1l1_opy_ (u"ࠧࡥࡧ࡯ࡥࡾ࠭৑")), str(bstack1111llll_opy_.get(bstack1l1_opy_ (u"ࠨࡴࡨࡶࡺࡴ࠭ࡥࡧ࡯ࡥࡾ࠭৒")))
            ]
    def bstack1lllll11l_opy_(self):
        bstack1lll1l1l1_opy_ = []
        for spec in self.bstack1lll1ll1l_opy_:
            bstack111l1111_opy_ = [spec]
            bstack111l1111_opy_ += self.bstack1lll11lll_opy_
            bstack1lll1l1l1_opy_.append(bstack111l1111_opy_)
        self.bstack1lll1l1l1_opy_ = bstack1lll1l1l1_opy_
        return bstack1lll1l1l1_opy_
    def bstack1lll1lll1_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111l1ll1_opy_ = True
            return True
        except Exception as e:
            self.bstack111l1ll1_opy_ = False
        return self.bstack111l1ll1_opy_
    def bstack1llllllll_opy_(self):
        bstack1l1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡇࡦࡶࠣࡸ࡭࡫ࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡸ࡭࡫࡭ࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡩ࡯ࡶ࠽ࠤ࡙࡮ࡥࠡࡶࡲࡸࡦࡲࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࡦࡳࡱࡲࡥࡤࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ৓")
        try:
            from browserstack_sdk.bstack11ll1lll_opy_ import bstack11ll1l11_opy_
            bstack1llll1l1l_opy_ = bstack11ll1l11_opy_(bstack11ll1l1l_opy_=self.bstack1lll11lll_opy_)
            if not bstack1llll1l1l_opy_.get(bstack1l1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ৔"), False):
                self.logger.error(bstack1l1_opy_ (u"࡙ࠦ࡫ࡳࡵࠢࡦࡳࡺࡴࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤ৕").format(bstack1llll1l1l_opy_.get(bstack1l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ৖"), bstack1l1_opy_ (u"࠭ࡕ࡯࡭ࡱࡳࡼࡴࠠࡦࡴࡵࡳࡷ࠭ৗ"))))
                return 0
            count = bstack1llll1l1l_opy_.get(bstack1l1_opy_ (u"ࠧࡤࡱࡸࡲࡹ࠭৘"), 0)
            test_files = bstack1llll1l1l_opy_.get(bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬ৙"), [])
            self.logger.info(bstack1l1_opy_ (u"ࠤࡗࡳࡹࡧ࡬ࠡࡶࡨࡷࡹࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦ࠽ࠤࢀࢃࠢ৚").format(count))
            return count
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢ৛").format(e))
            return 0
    def bstack1lll11ll1_opy_(self, bstack111ll1l1_opy_, bstack1llllll1l_opy_):
        bstack1llllll1l_opy_[bstack1l1_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫড়")] = self.bstack11111l11_opy_
        multiprocessing.set_start_method(bstack1l1_opy_ (u"ࠬࡹࡰࡢࡹࡱࠫঢ়"))
        bstack111l1lll_opy_ = []
        manager = multiprocessing.Manager()
        bstack1llll11ll_opy_ = manager.list()
        if bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৞") in self.bstack11111l11_opy_:
            for index, platform in enumerate(self.bstack11111l11_opy_[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪয়")]):
                bstack111l1lll_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack111ll1l1_opy_,
                                                            args=(self.bstack1lll11lll_opy_, bstack1llllll1l_opy_, bstack1llll11ll_opy_)))
            bstack1111l1l1_opy_ = len(self.bstack11111l11_opy_[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫৠ")])
        else:
            bstack111l1lll_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack111ll1l1_opy_,
                                                        args=(self.bstack1lll11lll_opy_, bstack1llllll1l_opy_, bstack1llll11ll_opy_)))
            bstack1111l1l1_opy_ = 1
        i = 0
        for t in bstack111l1lll_opy_:
            os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩৡ")] = str(i)
            if bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ৢ") in self.bstack11111l11_opy_:
                os.environ[bstack1l1_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬৣ")] = json.dumps(self.bstack11111l11_opy_[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৤")][i % bstack1111l1l1_opy_])
            i += 1
            t.start()
        for t in bstack111l1lll_opy_:
            t.join()
        return list(bstack1llll11ll_opy_)
    @staticmethod
    def bstack1lllllll1_opy_(driver, bstack1lll1l1ll_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ৥"), None)
        if item and getattr(item, bstack1l1_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࠩ০"), None) and not getattr(item, bstack1l1_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࡤࡪ࡯࡯ࡧࠪ১"), False):
            logger.info(
                bstack1l1_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠠࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡵࡻࡦࡿ࠮ࠣ২"))
            bstack111111l1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack11l1111l_opy_.bstack111ll11l_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack11111l1l_opy_(self):
        bstack1l1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡸࡴࠦࡢࡦࠢࡨࡼࡪࡩࡵࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ৩")
        try:
            from browserstack_sdk.bstack11ll1lll_opy_ import bstack11ll1l11_opy_
            bstack1lll1ll11_opy_ = bstack11ll1l11_opy_(bstack11ll1l1l_opy_=self.bstack1lll11lll_opy_)
            if not bstack1lll1ll11_opy_.get(bstack1l1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ৪"), False):
                self.logger.error(bstack1l1_opy_ (u"࡚ࠧࡥࡴࡶࠣࡪ࡮ࡲࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤ৫").format(bstack1lll1ll11_opy_.get(bstack1l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ৬"), bstack1l1_opy_ (u"ࠧࡖࡰ࡮ࡲࡴࡽ࡮ࠡࡧࡵࡶࡴࡸࠧ৭"))))
                return []
            test_files = bstack1lll1ll11_opy_.get(bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬ৮"), [])
            count = bstack1lll1ll11_opy_.get(bstack1l1_opy_ (u"ࠩࡦࡳࡺࡴࡴࠨ৯"), 0)
            self.logger.debug(bstack1l1_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷࡩࡩࠦࡻࡾࠢࡷࡩࡸࡺࡳࠡ࡫ࡱࠤࢀࢃࠠࡧ࡫࡯ࡩࡸࠨৰ").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦৱ").format(e))
            return []