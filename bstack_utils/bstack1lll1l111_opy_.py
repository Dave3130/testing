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
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1ll1l11_opy_ import bstack11ll1l11l11_opy_
from bstack_utils.bstack1111111l_opy_ import bstack1llllll11_opy_
from bstack_utils.helper import bstack11l1ll11l_opy_
import json
class bstack111lll11_opy_:
    _1ll1l1lll1l_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111ll111l_opy_ = bstack11ll1l11l11_opy_(self.config, logger)
        self.bstack1111111l_opy_ = bstack1llllll11_opy_.bstack1lll11ll1_opy_(config=self.config)
        self.bstack11111lll111_opy_ = {}
        self.bstack111l1ll1_opy_ = False
        self.bstack11111ll1l1l_opy_ = (
            self.__11111ll11l1_opy_()
            and self.bstack1111111l_opy_ is not None
            and self.bstack1111111l_opy_.bstack1lll1l11l_opy_()
            and config.get(bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪờ"), None) is not None
            and config.get(bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩỞ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1lll11ll1_opy_(cls, config, logger):
        if cls._1ll1l1lll1l_opy_ is None and config is not None:
            cls._1ll1l1lll1l_opy_ = bstack111lll11_opy_(config, logger)
        return cls._1ll1l1lll1l_opy_
    def bstack1lll1l11l_opy_(self):
        bstack11ll1ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡉࡵࠠ࡯ࡱࡷࠤࡦࡶࡰ࡭ࡻࠣࡸࡪࡹࡴࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡻ࡭࡫࡮࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡐ࠳࠴ࡽࠥ࡯ࡳࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡔࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡩࡴࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠣ࡭ࡸࠦࡎࡰࡰࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠥ࡯ࡳࠡࡐࡲࡲࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥở")
        return self.bstack11111ll1l1l_opy_ and self.bstack11111lll11l_opy_()
    def bstack11111lll11l_opy_(self):
        bstack11111ll1111_opy_ = os.getenv(bstack11ll1ll_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩỠ"), self.config.get(bstack11ll1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬỡ"), None))
        return bstack11111ll1111_opy_ in bstack11l11l1l11l_opy_
    def __11111ll11l1_opy_(self):
        bstack11ll11l11l1_opy_ = False
        for fw in bstack11l11ll1l11_opy_:
            if fw in self.config.get(bstack11ll1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭Ợ"), bstack11ll1ll_opy_ (u"ࠫࠬợ")):
                bstack11ll11l11l1_opy_ = True
        return bstack11l1ll11l_opy_(self.config.get(bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩỤ"), bstack11ll11l11l1_opy_))
    def bstack11111ll1ll1_opy_(self):
        return (not self.bstack1lll1l11l_opy_() and
                self.bstack1111111l_opy_ is not None and self.bstack1111111l_opy_.bstack1lll1l11l_opy_())
    def bstack11111ll11ll_opy_(self):
        if not self.bstack11111ll1ll1_opy_():
            return
        if self.config.get(bstack11ll1ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫụ"), None) is None or self.config.get(bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪỦ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11ll1ll_opy_ (u"ࠣࡖࡨࡷࡹࠦࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡧࡦࡴࠧࡵࠢࡺࡳࡷࡱࠠࡢࡵࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠦ࡯ࡳࠢࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠠࡪࡵࠣࡲࡺࡲ࡬࠯ࠢࡓࡰࡪࡧࡳࡦࠢࡶࡩࡹࠦࡡࠡࡰࡲࡲ࠲ࡴࡵ࡭࡮ࠣࡺࡦࡲࡵࡦ࠰ࠥủ"))
        if not self.__11111ll11l1_opy_():
            self.logger.info(bstack11ll1ll_opy_ (u"ࠤࡗࡩࡸࡺࠠࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡨࡧ࡮ࠨࡶࠣࡻࡴࡸ࡫ࠡࡣࡶࠤࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࠤ࡮ࡹࠠࡥ࡫ࡶࡥࡧࡲࡥࡥ࠰ࠣࡔࡱ࡫ࡡࡴࡧࠣࡩࡳࡧࡢ࡭ࡧࠣ࡭ࡹࠦࡦࡳࡱࡰࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠠࡧ࡫࡯ࡩ࠳ࠨỨ"))
    def bstack11111ll1l11_opy_(self):
        return self.bstack111l1ll1_opy_
    def bstack111111ll_opy_(self, bstack11111ll1lll_opy_):
        self.bstack111l1ll1_opy_ = bstack11111ll1lll_opy_
        self.bstack1111l11l_opy_(bstack11ll1ll_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡧࡧࠦứ"), bstack11111ll1lll_opy_)
    def bstack1111llll_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡠࡸࡥࡰࡴࡧࡩࡷࡥࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࡠࠤࡓࡵࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡰࡴࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫࠳ࠨỪ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1111111l_opy_.bstack111lllll1l1_opy_()
            if self.bstack1111111l_opy_ is not None:
                orchestration_strategy = self.bstack1111111l_opy_.bstack11l1ll1l1_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11ll1ll_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡴࡳࡣࡷࡩ࡬ࡿࠠࡪࡵࠣࡒࡴࡴࡥ࠯ࠢࡆࡥࡳࡴ࡯ࡵࠢࡳࡶࡴࡩࡥࡦࡦࠣࡻ࡮ࡺࡨࠡࡶࡨࡷࡹࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴ࠮ࠣừ"))
                return None
            self.logger.info(bstack11ll1ll_opy_ (u"ࠨࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡸ࡫ࡷ࡬ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡴࡳࡣࡷࡩ࡬ࡿ࠺ࠡࡽࢀࠦỬ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡖࡵ࡬ࡲ࡬ࠦࡃࡍࡋࠣࡪࡱࡵࡷࠡࡨࡲࡶࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥử"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡗࡶ࡭ࡳ࡭ࠠࡴࡦ࡮ࠤ࡫ࡲ࡯ࡸࠢࡩࡳࡷࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦỮ"))
                self.bstack11111ll111l_opy_.bstack11ll1lll111_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111ll111l_opy_.bstack11ll1l1l11l_opy_()
            if not ordered_test_files:
                return None
            self.bstack1111l11l_opy_(bstack11ll1ll_opy_ (u"ࠤࡸࡴࡱࡵࡡࡥࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡉ࡯ࡶࡰࡷࠦữ"), len(test_files))
            self.bstack1111l11l_opy_(bstack11ll1ll_opy_ (u"ࠥࡲࡴࡪࡥࡊࡰࡧࡩࡽࠨỰ"), int(os.environ.get(bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡒࡔࡊࡅࡠࡋࡑࡈࡊ࡞ࠢự")) or bstack11ll1ll_opy_ (u"ࠧ࠶ࠢỲ")))
            self.bstack1111l11l_opy_(bstack11ll1ll_opy_ (u"ࠨࡴࡰࡶࡤࡰࡓࡵࡤࡦࡵࠥỳ"), int(os.environ.get(bstack11ll1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥỴ")) or bstack11ll1ll_opy_ (u"ࠣ࠳ࠥỵ")))
            self.bstack1111l11l_opy_(bstack11ll1ll_opy_ (u"ࠤࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳࡄࡱࡸࡲࡹࠨỶ"), len(ordered_test_files))
            self.bstack1111l11l_opy_(bstack11ll1ll_opy_ (u"ࠥࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹࡁࡑࡋࡆࡥࡱࡲࡃࡰࡷࡱࡸࠧỷ"), self.bstack11111ll111l_opy_.bstack11ll1ll1l1l_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡠࡸࡥࡰࡴࡧࡩࡷࡥࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࡠࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣ࡭ࡣࡶࡷࡪࡹ࠺ࠡࡽࢀࠦỸ").format(e))
        return None
    def bstack1111l11l_opy_(self, key, value):
        self.bstack11111lll111_opy_[key] = value
    def bstack11111l11ll_opy_(self):
        return self.bstack11111lll111_opy_