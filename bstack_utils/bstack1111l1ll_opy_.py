# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1llll11_opy_ import bstack11ll1ll11l1_opy_
from bstack_utils.bstack1lll1llll_opy_ import bstack1llll1lll_opy_
from bstack_utils.helper import bstack11l1llll1_opy_
import json
class bstack111111ll_opy_:
    _1ll1l1lll1l_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111ll1lll_opy_ = bstack11ll1ll11l1_opy_(self.config, logger)
        self.bstack1lll1llll_opy_ = bstack1llll1lll_opy_.bstack1111ll1l_opy_(config=self.config)
        self.bstack1111l111111_opy_ = {}
        self.bstack111lll11_opy_ = False
        self.bstack11111llllll_opy_ = (
            self.__11111lllll1_opy_()
            and self.bstack1lll1llll_opy_ is not None
            and self.bstack1lll1llll_opy_.bstack11111l1l_opy_()
            and config.get(bstack111l1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫẦ"), None) is not None
            and config.get(bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪầ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1111ll1l_opy_(cls, config, logger):
        if cls._1ll1l1lll1l_opy_ is None and config is not None:
            cls._1ll1l1lll1l_opy_ = bstack111111ll_opy_(config, logger)
        return cls._1ll1l1lll1l_opy_
    def bstack11111l1l_opy_(self):
        bstack111l1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡊ࡯ࠡࡰࡲࡸࠥࡧࡰࡱ࡮ࡼࠤࡹ࡫ࡳࡵࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡼ࡮ࡥ࡯࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡑ࠴࠵ࡾࠦࡩࡴࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡕࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡪࡵࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠦࡩࡴࠢࡑࡳࡳ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦẨ")
        return self.bstack11111llllll_opy_ and self.bstack11111lll1ll_opy_()
    def bstack11111lll1ll_opy_(self):
        bstack11111llll1l_opy_ = os.getenv(bstack111l1l_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪẩ"), self.config.get(bstack111l1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭Ẫ"), None))
        return bstack11111llll1l_opy_ in bstack11l11l1l1l1_opy_
    def __11111lllll1_opy_(self):
        bstack11ll11ll1l1_opy_ = False
        for fw in bstack11l11ll1111_opy_:
            if fw in self.config.get(bstack111l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧẫ"), bstack111l1l_opy_ (u"ࠬ࠭Ậ")):
                bstack11ll11ll1l1_opy_ = True
        return bstack11l1llll1_opy_(self.config.get(bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪậ"), bstack11ll11ll1l1_opy_))
    def bstack11111llll11_opy_(self):
        return (not self.bstack11111l1l_opy_() and
                self.bstack1lll1llll_opy_ is not None and self.bstack1lll1llll_opy_.bstack11111l1l_opy_())
    def bstack11111lll111_opy_(self):
        if not self.bstack11111llll11_opy_():
            return
        if self.config.get(bstack111l1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬẮ"), None) is None or self.config.get(bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫắ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack111l1l_opy_ (u"ࠤࡗࡩࡸࡺࠠࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡨࡧ࡮ࠨࡶࠣࡻࡴࡸ࡫ࠡࡣࡶࠤࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠠࡰࡴࠣࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠡ࡫ࡶࠤࡳࡻ࡬࡭࠰ࠣࡔࡱ࡫ࡡࡴࡧࠣࡷࡪࡺࠠࡢࠢࡱࡳࡳ࠳࡮ࡶ࡮࡯ࠤࡻࡧ࡬ࡶࡧ࠱ࠦẰ"))
        if not self.__11111lllll1_opy_():
            self.logger.info(bstack111l1l_opy_ (u"ࠥࡘࡪࡹࡴࠡࡔࡨࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡩࡡ࡯ࠩࡷࠤࡼࡵࡲ࡬ࠢࡤࡷࠥࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦ࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡪࡴࡡࡣ࡮ࡨࠤ࡮ࡺࠠࡧࡴࡲࡱࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠡࡨ࡬ࡰࡪ࠴ࠢằ"))
    def bstack11111lll1l1_opy_(self):
        return self.bstack111lll11_opy_
    def bstack1lll1111l_opy_(self, bstack11111lll11l_opy_):
        self.bstack111lll11_opy_ = bstack11111lll11l_opy_
        self.bstack111lll1l_opy_(bstack111l1l_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡨࡨࠧẲ"), bstack11111lll11l_opy_)
    def bstack111ll111_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack111l1l_opy_ (u"ࠧࡡࡲࡦࡱࡵࡨࡪࡸ࡟ࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࡡࠥࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡶࡲࡰࡸ࡬ࡨࡪࡪࠠࡧࡱࡵࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬࠴ࠢẳ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1lll1llll_opy_.bstack11l1111l11l_opy_()
            if self.bstack1lll1llll_opy_ is not None:
                orchestration_strategy = self.bstack1lll1llll_opy_.bstack11ll111ll_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack111l1l_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡵࡴࡤࡸࡪ࡭ࡹࠡ࡫ࡶࠤࡓࡵ࡮ࡦ࠰ࠣࡇࡦࡴ࡮ࡰࡶࠣࡴࡷࡵࡣࡦࡧࡧࠤࡼ࡯ࡴࡩࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠯ࠤẴ"))
                return None
            self.logger.info(bstack111l1l_opy_ (u"ࠢࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡹ࡬ࡸ࡭ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡵࡴࡤࡸࡪ࡭ࡹ࠻ࠢࡾࢁࠧẵ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack111l1l_opy_ (u"ࠣࡗࡶ࡭ࡳ࡭ࠠࡄࡎࡌࠤ࡫ࡲ࡯ࡸࠢࡩࡳࡷࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦẶ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack111l1l_opy_ (u"ࠤࡘࡷ࡮ࡴࡧࠡࡵࡧ࡯ࠥ࡬࡬ࡰࡹࠣࡪࡴࡸࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠲ࠧặ"))
                self.bstack11111ll1lll_opy_.bstack11ll1ll1ll1_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111ll1lll_opy_.bstack11ll1lllll1_opy_()
            if not ordered_test_files:
                return None
            self.bstack111lll1l_opy_(bstack111l1l_opy_ (u"ࠥࡹࡵࡲ࡯ࡢࡦࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹࡃࡰࡷࡱࡸࠧẸ"), len(test_files))
            self.bstack111lll1l_opy_(bstack111l1l_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢẹ"), int(os.environ.get(bstack111l1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣẺ")) or bstack111l1l_opy_ (u"ࠨ࠰ࠣẻ")))
            self.bstack111lll1l_opy_(bstack111l1l_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦẼ"), int(os.environ.get(bstack111l1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦẽ")) or bstack111l1l_opy_ (u"ࠤ࠴ࠦẾ")))
            self.bstack111lll1l_opy_(bstack111l1l_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴࡅࡲࡹࡳࡺࠢế"), len(ordered_test_files))
            self.bstack111lll1l_opy_(bstack111l1l_opy_ (u"ࠦࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳࡂࡒࡌࡇࡦࡲ࡬ࡄࡱࡸࡲࡹࠨỀ"), self.bstack11111ll1lll_opy_.bstack11ll1l1l1ll_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack111l1l_opy_ (u"ࠧࡡࡲࡦࡱࡵࡨࡪࡸ࡟ࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࡡࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤ࡮ࡤࡷࡸ࡫ࡳ࠻ࠢࡾࢁࠧề").format(e))
        return None
    def bstack111lll1l_opy_(self, key, value):
        self.bstack1111l111111_opy_[key] = value
    def bstack1l111ll11_opy_(self):
        return self.bstack1111l111111_opy_