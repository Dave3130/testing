# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack111llll1_opy_
from browserstack_sdk.bstack1llll111l_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1lllll11l_opy_
from bstack_utils.bstack111lll1l_opy_ import bstack1lll11ll1_opy_
from bstack_utils.constants import bstack1lll1llll_opy_
from bstack_utils.bstack1llll1l11_opy_ import bstack1llllll1l_opy_
class bstack1lll1ll1l_opy_:
    def __init__(self, args, logger, bstack1111l111_opy_, bstack111l1lll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l111_opy_ = bstack1111l111_opy_
        self.bstack111l1lll_opy_ = bstack111l1lll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack111l111l_opy_ = []
        self.bstack1lllll111_opy_ = []
        self.bstack1111ll11_opy_ = []
        self.bstack1lll1lll1_opy_ = self.bstack1111llll_opy_()
        self.bstack111l1ll1_opy_ = -1
    def bstack1lllll1l1_opy_(self, bstack1llll1lll_opy_):
        self.parse_args()
        self.bstack11111l11_opy_()
        self.bstack11111ll1_opy_(bstack1llll1lll_opy_)
        self.bstack111l1l11_opy_()
    def bstack1lll1l1ll_opy_(self):
        bstack1llll1l11_opy_ = bstack1llllll1l_opy_.bstack1llll1ll1_opy_(self.bstack1111l111_opy_, self.logger)
        if bstack1llll1l11_opy_ is None:
            self.logger.warn(bstack11l11l1_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡲࡩࡲࡥࡳࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦয"))
            return
        bstack111ll1ll_opy_ = False
        bstack1llll1l11_opy_.bstack1111l1ll_opy_(bstack11l11l1_opy_ (u"ࠤࡨࡲࡦࡨ࡬ࡦࡦࠥর"), bstack1llll1l11_opy_.bstack111ll111_opy_())
        start_time = time.time()
        if bstack1llll1l11_opy_.bstack111ll111_opy_():
            test_files = self.bstack111ll1l1_opy_()
            bstack111ll1ll_opy_ = True
            bstack11111lll_opy_ = bstack1llll1l11_opy_.bstack1111111l_opy_(test_files)
            if bstack11111lll_opy_:
                self.bstack111l111l_opy_ = [os.path.normpath(item).replace(bstack11l11l1_opy_ (u"ࠪࡠࡡ࠭঱"), bstack11l11l1_opy_ (u"ࠫ࠴࠭ল")) for item in bstack11111lll_opy_]
                self.__1llll1l1l_opy_()
                bstack1llll1l11_opy_.bstack11111l1l_opy_(bstack111ll1ll_opy_)
                self.logger.info(bstack11l11l1_opy_ (u"࡚ࠧࡥࡴࡶࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡶࡵ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥ঳").format(self.bstack111l111l_opy_))
            else:
                self.logger.info(bstack11l11l1_opy_ (u"ࠨࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡦࡴࡨࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡣࡻࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦ঴"))
        bstack1llll1l11_opy_.bstack1111l1ll_opy_(bstack11l11l1_opy_ (u"ࠢࡵ࡫ࡰࡩ࡙ࡧ࡫ࡦࡰࡗࡳࡆࡶࡰ࡭ࡻࠥ঵"), int((time.time() - start_time) * 1000)) # bstack1111l1l1_opy_ to bstack1llllllll_opy_
    def __1llll1l1l_opy_(self):
        bstack11l11l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡱ࡮ࡤࡧࡪࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࠢࡳࡥࡹ࡮ࡳࠡ࡫ࡱࠤࡈࡒࡉࠡࡨ࡯ࡥ࡬ࡹࠠࡸ࡫ࡷ࡬ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵࡧࡧࠤ࡫࡯࡬ࡦࠢࡳࡥࡹ࡮ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡪࡸࡶࡦࡴࠣࡶࡪࡺࡵࡳࡰࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡧ࡫࡯ࡩࠥࡴࡡ࡮ࡧࡶ࠰ࠥࡧ࡮ࡥࠢࡺࡩࠥࡹࡩ࡮ࡲ࡯ࡽࠥࡻࡰࡥࡣࡷࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࡴࡩࡧࠣࡇࡑࡏࠠࡢࡴࡪࡷࠥࡺ࡯ࠡࡷࡶࡩࠥࡺࡨࡰࡵࡨࠤ࡫࡯࡬ࡦࡵ࠱ࠤ࡚ࡹࡥࡳࠩࡶࠤ࡫࡯࡬ࡵࡧࡵ࡭ࡳ࡭ࠠࡧ࡮ࡤ࡫ࡸࠦࠨ࠮࡯࠯ࠤ࠲ࡱࠩࠡࡴࡨࡱࡦ࡯࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࡹࡧࡣࡵࠢࡤࡲࡩࠦࡷࡪ࡮࡯ࠤࡧ࡫ࠠࡢࡲࡳࡰ࡮࡫ࡤࠡࡰࡤࡸࡺࡸࡡ࡭࡮ࡼࠤࡩࡻࡲࡪࡰࡪࠤࡵࡿࡴࡦࡵࡷࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨশ")
        try:
            if not self.bstack111l111l_opy_:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡑࡳࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡴࡦࡺࡨࠡࡶࡲࠤࡸ࡫ࡴࠣষ"))
                return
            bstack111lllll_opy_ = []
            bstack1lll1l11l_opy_ = []
            for flag in self.bstack1lllll111_opy_:
                if flag.startswith(bstack11l11l1_opy_ (u"ࠪ࠱ࠬস")):
                    bstack111lllll_opy_.append(flag)
                    continue
                bstack1lllll1ll_opy_ = False
                if bstack11l11l1_opy_ (u"ࠫ࠿ࡀࠧহ") in flag:
                    bstack1lllll1ll_opy_ = True
                elif flag.endswith(bstack11l11l1_opy_ (u"ࠬ࠴ࡰࡺࠩ঺")):
                    bstack1lllll1ll_opy_ = True
                elif os.path.exists(flag):
                    if os.path.isdir(flag) or (os.path.isfile(flag) and flag.endswith(bstack11l11l1_opy_ (u"࠭࠮ࡱࡻࠪ঻"))):
                        bstack1lllll1ll_opy_ = True
                if not bstack1lllll1ll_opy_:
                    bstack111lllll_opy_.append(flag)
                else:
                    bstack1lll1l11l_opy_.append(flag)
            bstack111lllll_opy_.extend(self.bstack111l111l_opy_)
            self.bstack1lllll111_opy_ = bstack111lllll_opy_
        except Exception as e:
            self.logger.error(bstack11l11l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡥࡥࠢࡶࡩࡱ࡫ࡣࡵࡱࡵࡷ࠿ࠦࡻࡾࠤ়").format(str(e)))
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1llll1111_opy_():
        import importlib
        if getattr(importlib, bstack11l11l1_opy_ (u"ࠨࡨ࡬ࡲࡩࡥ࡬ࡰࡣࡧࡩࡷ࠭ঽ"), False):
            bstack111111ll_opy_ = importlib.find_loader(bstack11l11l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫা"))
        else:
            bstack111111ll_opy_ = importlib.util.find_spec(bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬি"))
    def bstack111111l1_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack111l1ll1_opy_ = -1
        if self.bstack111l1lll_opy_ and bstack11l11l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫী") in self.bstack1111l111_opy_:
            self.bstack111l1ll1_opy_ = int(self.bstack1111l111_opy_[bstack11l11l1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬু")])
        try:
            bstack111lll11_opy_ = [bstack11l11l1_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨূ"), bstack11l11l1_opy_ (u"ࠧ࠮࠯ࡳࡰࡺ࡭ࡩ࡯ࡵࠪৃ"), bstack11l11l1_opy_ (u"ࠨ࠯ࡳࠫৄ")]
            if self.bstack111l1ll1_opy_ >= 0:
                bstack111lll11_opy_.extend([bstack11l11l1_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ৅"), bstack11l11l1_opy_ (u"ࠪ࠱ࡳ࠭৆")])
            for arg in bstack111lll11_opy_:
                self.bstack111111l1_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11111l11_opy_(self):
        bstack1lllll111_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1lllll111_opy_ = bstack1lllll111_opy_
        return self.bstack1lllll111_opy_
    def bstack1lll1l1l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1llll1111_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1lllll11l_opy_)
    def bstack11111ll1_opy_(self, bstack1llll1lll_opy_):
        bstack11111111_opy_ = Config.bstack1llll1ll1_opy_()
        if bstack1llll1lll_opy_:
            self.bstack1lllll111_opy_.append(bstack11l11l1_opy_ (u"ࠫ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨে"))
            self.bstack1lllll111_opy_.append(bstack11l11l1_opy_ (u"࡚ࠬࡲࡶࡧࠪৈ"))
        if bstack11111111_opy_.bstack111l1111_opy_():
            self.bstack1lllll111_opy_.append(bstack11l11l1_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬ৉"))
            self.bstack1lllll111_opy_.append(bstack11l11l1_opy_ (u"ࠧࡕࡴࡸࡩࠬ৊"))
        self.bstack1lllll111_opy_.append(bstack11l11l1_opy_ (u"ࠨ࠯ࡳࠫো"))
        self.bstack1lllll111_opy_.append(bstack11l11l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠧৌ"))
        self.bstack1lllll111_opy_.append(bstack11l11l1_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶ্ࠬ"))
        self.bstack1lllll111_opy_.append(bstack11l11l1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫৎ"))
        if self.bstack111l1ll1_opy_ > 1:
            self.bstack1lllll111_opy_.append(bstack11l11l1_opy_ (u"ࠬ࠳࡮ࠨ৏"))
            self.bstack1lllll111_opy_.append(str(self.bstack111l1ll1_opy_))
    def bstack111l1l11_opy_(self):
        if bstack1lll11ll1_opy_.bstack1lll1ll11_opy_(self.bstack1111l111_opy_):
             self.bstack1lllll111_opy_ += [
                bstack1lll1llll_opy_.get(bstack11l11l1_opy_ (u"࠭ࡲࡦࡴࡸࡲࠬ৐")), str(bstack1lll11ll1_opy_.bstack1111lll1_opy_(self.bstack1111l111_opy_)),
                bstack1lll1llll_opy_.get(bstack11l11l1_opy_ (u"ࠧࡥࡧ࡯ࡥࡾ࠭৑")), str(bstack1lll1llll_opy_.get(bstack11l11l1_opy_ (u"ࠨࡴࡨࡶࡺࡴ࠭ࡥࡧ࡯ࡥࡾ࠭৒")))
            ]
    def bstack1lll11l1l_opy_(self):
        bstack1111ll11_opy_ = []
        for spec in self.bstack111l111l_opy_:
            bstack11l11111_opy_ = [spec]
            bstack11l11111_opy_ += self.bstack1lllll111_opy_
            bstack1111ll11_opy_.append(bstack11l11111_opy_)
        self.bstack1111ll11_opy_ = bstack1111ll11_opy_
        return bstack1111ll11_opy_
    def bstack1111llll_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1lll1lll1_opy_ = True
            return True
        except Exception as e:
            self.bstack1lll1lll1_opy_ = False
        return self.bstack1lll1lll1_opy_
    def bstack111l11ll_opy_(self):
        bstack11l11l1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡇࡦࡶࠣࡸ࡭࡫ࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡸ࡭࡫࡭ࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡩ࡯ࡶ࠽ࠤ࡙࡮ࡥࠡࡶࡲࡸࡦࡲࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࡦࡳࡱࡲࡥࡤࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ৓")
        try:
            from browserstack_sdk.bstack11ll111l_opy_ import bstack11ll1ll1_opy_
            bstack1lll1l111_opy_ = bstack11ll1ll1_opy_(bstack11ll11ll_opy_=self.bstack1lllll111_opy_)
            if not bstack1lll1l111_opy_.get(bstack11l11l1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ৔"), False):
                self.logger.error(bstack11l11l1_opy_ (u"࡙ࠦ࡫ࡳࡵࠢࡦࡳࡺࡴࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤ৕").format(bstack1lll1l111_opy_.get(bstack11l11l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ৖"), bstack11l11l1_opy_ (u"࠭ࡕ࡯࡭ࡱࡳࡼࡴࠠࡦࡴࡵࡳࡷ࠭ৗ"))))
                return 0
            count = bstack1lll1l111_opy_.get(bstack11l11l1_opy_ (u"ࠧࡤࡱࡸࡲࡹ࠭৘"), 0)
            test_files = bstack1lll1l111_opy_.get(bstack11l11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬ৙"), [])
            self.logger.info(bstack11l11l1_opy_ (u"ࠤࡗࡳࡹࡧ࡬ࠡࡶࡨࡷࡹࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦ࠽ࠤࢀࢃࠢ৚").format(count))
            return count
        except Exception as e:
            self.logger.error(bstack11l11l1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢ৛").format(e))
            return 0
    def bstack1llll11l1_opy_(self, bstack1llllll11_opy_, bstack1lllll1l1_opy_):
        bstack1lllll1l1_opy_[bstack11l11l1_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫড়")] = self.bstack1111l111_opy_
        multiprocessing.set_start_method(bstack11l11l1_opy_ (u"ࠬࡹࡰࡢࡹࡱࠫঢ়"))
        bstack1111ll1l_opy_ = []
        manager = multiprocessing.Manager()
        bstack1lllllll1_opy_ = manager.list()
        if bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৞") in self.bstack1111l111_opy_:
            for index, platform in enumerate(self.bstack1111l111_opy_[bstack11l11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪয়")]):
                bstack1111ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1llllll11_opy_,
                                                            args=(self.bstack1lllll111_opy_, bstack1lllll1l1_opy_, bstack1lllllll1_opy_)))
            bstack111l11l1_opy_ = len(self.bstack1111l111_opy_[bstack11l11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫৠ")])
        else:
            bstack1111ll1l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1llllll11_opy_,
                                                        args=(self.bstack1lllll111_opy_, bstack1lllll1l1_opy_, bstack1lllllll1_opy_)))
            bstack111l11l1_opy_ = 1
        i = 0
        for t in bstack1111ll1l_opy_:
            os.environ[bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩৡ")] = str(i)
            if bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ৢ") in self.bstack1111l111_opy_:
                os.environ[bstack11l11l1_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬৣ")] = json.dumps(self.bstack1111l111_opy_[bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৤")][i % bstack111l11l1_opy_])
            i += 1
            t.start()
        for t in bstack1111ll1l_opy_:
            t.join()
        return list(bstack1lllllll1_opy_)
    @staticmethod
    def bstack111l1l1l_opy_(driver, bstack1lll11lll_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11l11l1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ৥"), None)
        if item and getattr(item, bstack11l11l1_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࠩ০"), None) and not getattr(item, bstack11l11l1_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࡤࡪ࡯࡯ࡧࠪ১"), False):
            logger.info(
                bstack11l11l1_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠠࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡵࡻࡦࡿ࠮ࠣ২"))
            bstack11l1111l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack111llll1_opy_.bstack111ll11l_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack111ll1l1_opy_(self):
        bstack11l11l1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡸࡴࠦࡢࡦࠢࡨࡼࡪࡩࡵࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ৩")
        try:
            from browserstack_sdk.bstack11ll111l_opy_ import bstack11ll1ll1_opy_
            bstack1llll11ll_opy_ = bstack11ll1ll1_opy_(bstack11ll11ll_opy_=self.bstack1lllll111_opy_)
            if not bstack1llll11ll_opy_.get(bstack11l11l1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ৪"), False):
                self.logger.error(bstack11l11l1_opy_ (u"࡚ࠧࡥࡴࡶࠣࡪ࡮ࡲࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤ৫").format(bstack1llll11ll_opy_.get(bstack11l11l1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ৬"), bstack11l11l1_opy_ (u"ࠧࡖࡰ࡮ࡲࡴࡽ࡮ࠡࡧࡵࡶࡴࡸࠧ৭"))))
                return []
            test_files = bstack1llll11ll_opy_.get(bstack11l11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬ৮"), [])
            count = bstack1llll11ll_opy_.get(bstack11l11l1_opy_ (u"ࠩࡦࡳࡺࡴࡴࠨ৯"), 0)
            self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷࡩࡩࠦࡻࡾࠢࡷࡩࡸࡺࡳࠡ࡫ࡱࠤࢀࢃࠠࡧ࡫࡯ࡩࡸࠨৰ").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l11l1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦৱ").format(e))
            return []