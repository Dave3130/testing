# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack11111111_opy_
from browserstack_sdk.bstack1lllll11l_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1111l1l1_opy_
from bstack_utils.bstack1llll11ll_opy_ import bstack1lll1ll1l_opy_
from bstack_utils.constants import bstack1llll11l1_opy_
from bstack_utils.bstack1lll11l1l_opy_ import bstack11111l1l_opy_
class bstack1lll111l1_opy_:
    def __init__(self, args, logger, bstack1lll1l111_opy_, bstack1lll11l11_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll1l111_opy_ = bstack1lll1l111_opy_
        self.bstack1lll11l11_opy_ = bstack1lll11l11_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11111l11_opy_ = []
        self.bstack1111l11l_opy_ = []
        self.bstack1lll111ll_opy_ = []
        self.bstack1llll1l11_opy_ = self.bstack1111l1ll_opy_()
        self.bstack111l1111_opy_ = -1
    def bstack11111lll_opy_(self, bstack1llll1l1l_opy_):
        self.parse_args()
        self.bstack1lll1llll_opy_()
        self.bstack1lll1l1l1_opy_(bstack1llll1l1l_opy_)
        self.bstack1111ll11_opy_()
    def bstack1llll1111_opy_(self):
        bstack1lll11l1l_opy_ = bstack11111l1l_opy_.bstack111l11l1_opy_(self.bstack1lll1l111_opy_, self.logger)
        if bstack1lll11l1l_opy_ is None:
            self.logger.warn(bstack1l111ll_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡲࡩࡲࡥࡳࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦশ"))
            return
        bstack1lll11ll1_opy_ = False
        bstack1lll11l1l_opy_.bstack1lll1111l_opy_(bstack1l111ll_opy_ (u"ࠤࡨࡲࡦࡨ࡬ࡦࡦࠥষ"), bstack1lll11l1l_opy_.bstack111l1l11_opy_())
        start_time = time.time()
        if bstack1lll11l1l_opy_.bstack111l1l11_opy_():
            test_files = self.bstack1llllll11_opy_()
            bstack1lll11ll1_opy_ = True
            bstack111ll1l1_opy_ = bstack1lll11l1l_opy_.bstack1lll1l1ll_opy_(test_files)
            if bstack111ll1l1_opy_:
                self.bstack11111l11_opy_ = [os.path.normpath(item).replace(bstack1l111ll_opy_ (u"ࠪࡠࡡ࠭স"), bstack1l111ll_opy_ (u"ࠫ࠴࠭হ")) for item in bstack111ll1l1_opy_]
                self.__111ll11l_opy_()
                bstack1lll11l1l_opy_.bstack111l1ll1_opy_(bstack1lll11ll1_opy_)
                self.logger.info(bstack1l111ll_opy_ (u"࡚ࠧࡥࡴࡶࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡶࡵ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥ঺").format(self.bstack11111l11_opy_))
            else:
                self.logger.info(bstack1l111ll_opy_ (u"ࠨࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡦࡴࡨࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡣࡻࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦ঻"))
        bstack1lll11l1l_opy_.bstack1lll1111l_opy_(bstack1l111ll_opy_ (u"ࠢࡵ࡫ࡰࡩ࡙ࡧ࡫ࡦࡰࡗࡳࡆࡶࡰ࡭ࡻ়ࠥ"), int((time.time() - start_time) * 1000)) # bstack1111l111_opy_ to bstack1lllll1ll_opy_
    def __111ll11l_opy_(self):
        bstack1l111ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡱ࡮ࡤࡧࡪࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࠢࡳࡥࡹ࡮ࡳࠡ࡫ࡱࠤࡈࡒࡉࠡࡨ࡯ࡥ࡬ࡹࠠࡸ࡫ࡷ࡬ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵࡧࡧࠤ࡫࡯࡬ࡦࠢࡳࡥࡹ࡮ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡪࡸࡶࡦࡴࠣࡶࡪࡺࡵࡳࡰࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡧ࡫࡯ࡩࠥࡴࡡ࡮ࡧࡶ࠰ࠥࡧ࡮ࡥࠢࡺࡩࠥࡹࡩ࡮ࡲ࡯ࡽࠥࡻࡰࡥࡣࡷࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࡴࡩࡧࠣࡇࡑࡏࠠࡢࡴࡪࡷࠥࡺ࡯ࠡࡷࡶࡩࠥࡺࡨࡰࡵࡨࠤ࡫࡯࡬ࡦࡵ࠱ࠤ࡚ࡹࡥࡳࠩࡶࠤ࡫࡯࡬ࡵࡧࡵ࡭ࡳ࡭ࠠࡧ࡮ࡤ࡫ࡸࠦࠨ࠮࡯࠯ࠤ࠲ࡱࠩࠡࡴࡨࡱࡦ࡯࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࡹࡧࡣࡵࠢࡤࡲࡩࠦࡷࡪ࡮࡯ࠤࡧ࡫ࠠࡢࡲࡳࡰ࡮࡫ࡤࠡࡰࡤࡸࡺࡸࡡ࡭࡮ࡼࠤࡩࡻࡲࡪࡰࡪࠤࡵࡿࡴࡦࡵࡷࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨঽ")
        try:
            if not self.bstack11111l11_opy_:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡑࡳࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡴࡦࡺࡨࠡࡶࡲࠤࡸ࡫ࡴࠣা"))
                return
            bstack1111llll_opy_ = []
            bstack1111lll1_opy_ = []
            for flag in self.bstack1111l11l_opy_:
                if flag.startswith(bstack1l111ll_opy_ (u"ࠪ࠱ࠬি")):
                    bstack1111llll_opy_.append(flag)
                    continue
                bstack1lll1lll1_opy_ = False
                if bstack1l111ll_opy_ (u"ࠫ࠿ࡀࠧী") in flag:
                    bstack1lll1lll1_opy_ = True
                elif flag.endswith(bstack1l111ll_opy_ (u"ࠬ࠴ࡰࡺࠩু")):
                    bstack1lll1lll1_opy_ = True
                elif os.path.exists(flag):
                    if os.path.isdir(flag) or (os.path.isfile(flag) and flag.endswith(bstack1l111ll_opy_ (u"࠭࠮ࡱࡻࠪূ"))):
                        bstack1lll1lll1_opy_ = True
                if not bstack1lll1lll1_opy_:
                    bstack1111llll_opy_.append(flag)
                else:
                    bstack1111lll1_opy_.append(flag)
            bstack1111llll_opy_.extend(self.bstack11111l11_opy_)
            self.bstack1111l11l_opy_ = bstack1111llll_opy_
            self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡖࡲࡧࡥࡹ࡫ࡤࠡࡅࡏࡍࠥ࡬࡬ࡢࡩࡶࠤࡦ࡬ࡴࡦࡴࠣࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠽ࠤࢀࢃࠢৃ").format(self.bstack1111l11l_opy_))
        except Exception as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡪࡺࡴࡪࡰࡪࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡦࡦࠣࡷࡪࡲࡥࡤࡶࡲࡶࡸࡀࠠࡼࡿࠥৄ").format(str(e)))
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1lll11lll_opy_():
        import importlib
        if getattr(importlib, bstack1l111ll_opy_ (u"ࠩࡩ࡭ࡳࡪ࡟࡭ࡱࡤࡨࡪࡸࠧ৅"), False):
            bstack1lllll1l1_opy_ = importlib.find_loader(bstack1l111ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ৆"))
        else:
            bstack1lllll1l1_opy_ = importlib.util.find_spec(bstack1l111ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ে"))
    def bstack1lllll111_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack111l1111_opy_ = -1
        if self.bstack1lll11l11_opy_ and bstack1l111ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬৈ") in self.bstack1lll1l111_opy_:
            self.bstack111l1111_opy_ = int(self.bstack1lll1l111_opy_[bstack1l111ll_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭৉")])
        try:
            bstack1111ll1l_opy_ = [bstack1l111ll_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩ৊"), bstack1l111ll_opy_ (u"ࠨ࠯࠰ࡴࡱࡻࡧࡪࡰࡶࠫো"), bstack1l111ll_opy_ (u"ࠩ࠰ࡴࠬৌ")]
            if self.bstack111l1111_opy_ >= 0:
                bstack1111ll1l_opy_.extend([bstack1l111ll_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶ্ࠫ"), bstack1l111ll_opy_ (u"ࠫ࠲ࡴࠧৎ")])
            for arg in bstack1111ll1l_opy_:
                self.bstack1lllll111_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1lll1llll_opy_(self):
        bstack1111l11l_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1111l11l_opy_ = bstack1111l11l_opy_
        return self.bstack1111l11l_opy_
    def bstack1llllll1l_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1lll11lll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1111l1l1_opy_)
    def bstack1lll1l1l1_opy_(self, bstack1llll1l1l_opy_):
        bstack111l11ll_opy_ = Config.bstack111l11l1_opy_()
        if bstack1llll1l1l_opy_:
            self.bstack1111l11l_opy_.append(bstack1l111ll_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ৏"))
            self.bstack1111l11l_opy_.append(bstack1l111ll_opy_ (u"࠭ࡔࡳࡷࡨࠫ৐"))
        if bstack111l11ll_opy_.bstack111l1lll_opy_():
            self.bstack1111l11l_opy_.append(bstack1l111ll_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭৑"))
            self.bstack1111l11l_opy_.append(bstack1l111ll_opy_ (u"ࠨࡖࡵࡹࡪ࠭৒"))
        self.bstack1111l11l_opy_.append(bstack1l111ll_opy_ (u"ࠩ࠰ࡴࠬ৓"))
        self.bstack1111l11l_opy_.append(bstack1l111ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠨ৔"))
        self.bstack1111l11l_opy_.append(bstack1l111ll_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭৕"))
        self.bstack1111l11l_opy_.append(bstack1l111ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ৖"))
        if self.bstack111l1111_opy_ > 1:
            self.bstack1111l11l_opy_.append(bstack1l111ll_opy_ (u"࠭࠭࡯ࠩৗ"))
            self.bstack1111l11l_opy_.append(str(self.bstack111l1111_opy_))
    def bstack1111ll11_opy_(self):
        if bstack1lll1ll1l_opy_.bstack1lllllll1_opy_(self.bstack1lll1l111_opy_):
             self.bstack1111l11l_opy_ += [
                bstack1llll11l1_opy_.get(bstack1l111ll_opy_ (u"ࠧࡳࡧࡵࡹࡳ࠭৘")), str(bstack1lll1ll1l_opy_.bstack111ll111_opy_(self.bstack1lll1l111_opy_)),
                bstack1llll11l1_opy_.get(bstack1l111ll_opy_ (u"ࠨࡦࡨࡰࡦࡿࠧ৙")), str(bstack1llll11l1_opy_.get(bstack1l111ll_opy_ (u"ࠩࡵࡩࡷࡻ࡮࠮ࡦࡨࡰࡦࡿࠧ৚")))
            ]
    def bstack1llll1lll_opy_(self):
        bstack1lll111ll_opy_ = []
        for spec in self.bstack11111l11_opy_:
            bstack111111ll_opy_ = [spec]
            bstack111111ll_opy_ += self.bstack1111l11l_opy_
            bstack1lll111ll_opy_.append(bstack111111ll_opy_)
        self.bstack1lll111ll_opy_ = bstack1lll111ll_opy_
        return bstack1lll111ll_opy_
    def bstack1111l1ll_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1llll1l11_opy_ = True
            return True
        except Exception as e:
            self.bstack1llll1l11_opy_ = False
        return self.bstack1llll1l11_opy_
    def bstack1lll1ll11_opy_(self):
        bstack1l111ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡈࡧࡷࠤࡹ࡮ࡥࠡࡥࡲࡹࡳࡺࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡹ࡮ࡥ࡮ࠢࡸࡷ࡮ࡴࡧࠡࡲࡼࡸࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡪࡰࡷ࠾࡚ࠥࡨࡦࠢࡷࡳࡹࡧ࡬ࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ৛")
        try:
            from browserstack_sdk.bstack11l1ll1l_opy_ import bstack11l1lll1_opy_
            bstack111111l1_opy_ = bstack11l1lll1_opy_(bstack11ll1lll_opy_=self.bstack1111l11l_opy_, bstack11ll1111_opy_=True)
            if not bstack111111l1_opy_.get(bstack1l111ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬড়"), False):
                self.logger.error(bstack1l111ll_opy_ (u"࡚ࠧࡥࡴࡶࠣࡧࡴࡻ࡮ࡵࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠥঢ়").format(bstack111111l1_opy_.get(bstack1l111ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ৞"), bstack1l111ll_opy_ (u"ࠧࡖࡰ࡮ࡲࡴࡽ࡮ࠡࡧࡵࡶࡴࡸࠧয়"))))
                return 0
            count = bstack111111l1_opy_.get(bstack1l111ll_opy_ (u"ࠨࡥࡲࡹࡳࡺࠧৠ"), 0)
            test_files = bstack111111l1_opy_.get(bstack1l111ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸ࠭ৡ"), [])
            self.logger.info(bstack1l111ll_opy_ (u"ࠥࡘࡴࡺࡡ࡭ࠢࡷࡩࡸࡺࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧ࠾ࠥࢁࡽࠣৢ").format(count))
            return count
        except Exception as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽࠣৣ").format(e))
            return 0
    def bstack111l111l_opy_(self, bstack1lll1l11l_opy_, bstack11111lll_opy_):
        bstack11111lll_opy_[bstack1l111ll_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ৤")] = self.bstack1lll1l111_opy_
        multiprocessing.set_start_method(bstack1l111ll_opy_ (u"࠭ࡳࡱࡣࡺࡲࠬ৥"))
        bstack1llll111l_opy_ = []
        manager = multiprocessing.Manager()
        bstack111l1l1l_opy_ = manager.list()
        if bstack1l111ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ০") in self.bstack1lll1l111_opy_:
            for index, platform in enumerate(self.bstack1lll1l111_opy_[bstack1l111ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ১")]):
                bstack1llll111l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1lll1l11l_opy_,
                                                            args=(self.bstack1111l11l_opy_, bstack11111lll_opy_, bstack111l1l1l_opy_)))
            bstack111ll1ll_opy_ = len(self.bstack1lll1l111_opy_[bstack1l111ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ২")])
        else:
            bstack1llll111l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1lll1l11l_opy_,
                                                        args=(self.bstack1111l11l_opy_, bstack11111lll_opy_, bstack111l1l1l_opy_)))
            bstack111ll1ll_opy_ = 1
        i = 0
        for t in bstack1llll111l_opy_:
            os.environ[bstack1l111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ৩")] = str(i)
            if bstack1l111ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ৪") in self.bstack1lll1l111_opy_:
                os.environ[bstack1l111ll_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭৫")] = json.dumps(self.bstack1lll1l111_opy_[bstack1l111ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৬")][i % bstack111ll1ll_opy_])
            i += 1
            t.start()
        for t in bstack1llll111l_opy_:
            t.join()
        return list(bstack111l1l1l_opy_)
    @staticmethod
    def bstack111lll1l_opy_(driver, bstack11111ll1_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1l111ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ৭"), None)
        if item and getattr(item, bstack1l111ll_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࠪ৮"), None) and not getattr(item, bstack1l111ll_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡳࡵࡥࡤࡰࡰࡨࠫ৯"), False):
            logger.info(
                bstack1l111ll_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠤৰ"))
            bstack111lll11_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack11111111_opy_.bstack1111111l_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1llllll11_opy_(self):
        bstack1l111ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡹࡵࠠࡣࡧࠣࡩࡽ࡫ࡣࡶࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥৱ")
        try:
            from browserstack_sdk.bstack11l1ll1l_opy_ import bstack11l1lll1_opy_
            bstack1llll1ll1_opy_ = bstack11l1lll1_opy_(bstack11ll1lll_opy_=self.bstack1111l11l_opy_, bstack11ll1111_opy_=True)
            if not bstack1llll1ll1_opy_.get(bstack1l111ll_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭৲"), False):
                self.logger.error(bstack1l111ll_opy_ (u"ࠨࡔࡦࡵࡷࠤ࡫࡯࡬ࡦࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠥ৳").format(bstack1llll1ll1_opy_.get(bstack1l111ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭৴"), bstack1l111ll_opy_ (u"ࠨࡗࡱ࡯ࡳࡵࡷ࡯ࠢࡨࡶࡷࡵࡲࠨ৵"))))
                return []
            test_files = bstack1llll1ll1_opy_.get(bstack1l111ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸ࠭৶"), [])
            count = bstack1llll1ll1_opy_.get(bstack1l111ll_opy_ (u"ࠪࡧࡴࡻ࡮ࡵࠩ৷"), 0)
            self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸࡪࡪࠠࡼࡿࠣࡸࡪࡹࡴࡴࠢ࡬ࡲࠥࢁࡽࠡࡨ࡬ࡰࡪࡹࠢ৸").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧ৹").format(e))
            return []