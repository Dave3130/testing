# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1llllll111l_opy_ import (
    bstack1llll1l1lll_opy_,
    bstack1111111l1l_opy_,
    bstack1111111111_opy_,
    bstack1lll1ll111l_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1llll11llll_opy_, bstack11ll1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1llllll11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_, bstack1lll1l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1l1_opy_ import bstack1lll1ll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l111_opy_ import bstack1lll1l111l1_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1111l1l11_opy_ import bstack1lll1ll11l_opy_, bstack11ll1111ll_opy_, bstack1ll1lllll_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1ll11ll_opy_(bstack1lll1l111l1_opy_):
    bstack1llll111l1l_opy_ = bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩࡸࡩࡷࡧࡵࡷࠧჺ")
    bstack1llll11l11l_opy_ = bstack11l1l11_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨ჻")
    bstack1lll1llllll_opy_ = bstack11l1l11_opy_ (u"ࠣࡰࡲࡲࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥჼ")
    bstack1lll1lll11l_opy_ = bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤჽ")
    bstack1llll11111l_opy_ = bstack11l1l11_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡡࡵࡩ࡫ࡹࠢჾ")
    bstack1llll111111_opy_ = bstack11l1l11_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡦࡶࡪࡧࡴࡦࡦࠥჿ")
    bstack1llll11lll1_opy_ = bstack11l1l11_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡲࡦࡳࡥࠣᄀ")
    bstack1lll1l1l1ll_opy_ = bstack11l1l11_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡸࡺࡡࡵࡷࡶࠦᄁ")
    def __init__(self):
        super().__init__(bstack1llll1l111l_opy_=self.bstack1llll111l1l_opy_, frameworks=[bstack1llllll11l1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack111111l11l_opy_((bstack1lll1lllll1_opy_.BEFORE_EACH, bstack1llll1111l1_opy_.POST), self.bstack1lll1l1llll_opy_)
        if bstack11ll1ll11_opy_():
            TestFramework.bstack111111l11l_opy_((bstack1lll1lllll1_opy_.TEST, bstack1llll1111l1_opy_.POST), self.bstack1lll1llll1l_opy_)
        else:
            TestFramework.bstack111111l11l_opy_((bstack1lll1lllll1_opy_.TEST, bstack1llll1111l1_opy_.PRE), self.bstack1lll1llll1l_opy_)
        TestFramework.bstack111111l11l_opy_((bstack1lll1lllll1_opy_.TEST, bstack1llll1111l1_opy_.POST), self.bstack1lll1lll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l1llll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        bstack1llll11ll1l_opy_ = self.bstack1lll1l1lll1_opy_(instance.context)
        if not bstack1llll11ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡵࡧࡧࡦ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᄂ") + str(bstack11111111l1_opy_) + bstack11l1l11_opy_ (u"ࠣࠤᄃ"))
            return
        f.bstack1llll1l1l1l_opy_(instance, bstack1lll1ll11ll_opy_.bstack1llll11l11l_opy_, bstack1llll11ll1l_opy_)
    def bstack1lll1l1lll1_opy_(self, context: bstack1lll1ll111l_opy_, bstack1llll11l111_opy_= True):
        if bstack1llll11l111_opy_:
            bstack1llll11ll1l_opy_ = self.bstack1lll1ll1111_opy_(context, reverse=True)
        else:
            bstack1llll11ll1l_opy_ = self.bstack1lll1l111ll_opy_(context, reverse=True)
        return [f for f in bstack1llll11ll1l_opy_ if f[1].state != bstack1llll1l1lll_opy_.QUIT]
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1llll_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
        if not bstack1llll11llll_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄄ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠥࠦᄅ"))
            return
        bstack1llll11ll1l_opy_ = f.get_state(instance, bstack1lll1ll11ll_opy_.bstack1llll11l11l_opy_, [])
        if not bstack1llll11ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄆ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠧࠨᄇ"))
            return
        if len(bstack1llll11ll1l_opy_) > 1:
            self.logger.debug(
                bstack1llll1111_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᄈ"))
        bstack1llll1l11l1_opy_, bstack1lll1l11l11_opy_ = bstack1llll11ll1l_opy_[0]
        page = bstack1llll1l11l1_opy_()
        if not page:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄉ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠣࠤᄊ"))
            return
        bstack111111ll1_opy_ = getattr(args[0], bstack11l1l11_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᄋ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᄌ")).get(bstack11l1l11_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᄍ")):
            try:
                page.evaluate(bstack11l1l11_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᄎ"),
                            bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪᄏ") + json.dumps(
                                bstack111111ll1_opy_) + bstack11l1l11_opy_ (u"ࠢࡾࡿࠥᄐ"))
            except Exception as e:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨᄑ"), e)
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1llll_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
        if not bstack1llll11llll_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄒ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠥࠦᄓ"))
            return
        bstack1llll11ll1l_opy_ = f.get_state(instance, bstack1lll1ll11ll_opy_.bstack1llll11l11l_opy_, [])
        if not bstack1llll11ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄔ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠧࠨᄕ"))
            return
        if len(bstack1llll11ll1l_opy_) > 1:
            self.logger.debug(
                bstack1llll1111_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᄖ"))
        bstack1llll1l11l1_opy_, bstack1lll1l11l11_opy_ = bstack1llll11ll1l_opy_[0]
        page = bstack1llll1l11l1_opy_()
        if not page:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄗ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠣࠤᄘ"))
            return
        status = f.get_state(instance, TestFramework.bstack1llll111ll1_opy_, None)
        if not status:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᄙ") + str(bstack11111111l1_opy_) + bstack11l1l11_opy_ (u"ࠥࠦᄚ"))
            return
        bstack1llll1111ll_opy_ = {bstack11l1l11_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᄛ"): status.lower()}
        bstack1llll1l1111_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll1ll1_opy_, None)
        if status.lower() == bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᄜ") and bstack1llll1l1111_opy_ is not None:
            bstack1llll1111ll_opy_[bstack11l1l11_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᄝ")] = bstack1llll1l1111_opy_[0][bstack11l1l11_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᄞ")][0] if isinstance(bstack1llll1l1111_opy_, list) else str(bstack1llll1l1111_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᄟ")).get(bstack11l1l11_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᄠ")):
            try:
                page.evaluate(
                        bstack11l1l11_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᄡ"),
                        bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࠩᄢ")
                        + json.dumps(bstack1llll1111ll_opy_)
                        + bstack11l1l11_opy_ (u"ࠧࢃࠢᄣ")
                    )
            except Exception as e:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡿࢂࠨᄤ"), e)
    def bstack1llll111lll_opy_(
        self,
        instance: bstack1lll1l1ll11_opy_,
        f: TestFramework,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1llll_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
        if not bstack1llll11llll_opy_:
            self.logger.debug(
                bstack1llll1111_opy_ (u"ࠢ࡮ࡣࡵ࡯ࡤࡵ࠱࠲ࡻࡢࡷࡾࡴࡣ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᄥ"))
            return
        bstack1llll11ll1l_opy_ = f.get_state(instance, bstack1lll1ll11ll_opy_.bstack1llll11l11l_opy_, [])
        if not bstack1llll11ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄦ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠤࠥᄧ"))
            return
        if len(bstack1llll11ll1l_opy_) > 1:
            self.logger.debug(
                bstack1llll1111_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧᄨ"))
        bstack1llll1l11l1_opy_, bstack1lll1l11l11_opy_ = bstack1llll11ll1l_opy_[0]
        page = bstack1llll1l11l1_opy_()
        if not page:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡲࡧࡲ࡬ࡡࡲ࠵࠶ࡿ࡟ࡴࡻࡱࡧ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄩ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠧࠨᄪ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack11l1l11_opy_ (u"ࠨࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࡙ࡹ࡯ࡥ࠽ࠦᄫ") + str(timestamp)
        try:
            page.evaluate(
                bstack11l1l11_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᄬ"),
                bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ᄭ").format(
                    json.dumps(
                        {
                            bstack11l1l11_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᄮ"): bstack11l1l11_opy_ (u"ࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧᄯ"),
                            bstack11l1l11_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᄰ"): {
                                bstack11l1l11_opy_ (u"ࠧࡺࡹࡱࡧࠥᄱ"): bstack11l1l11_opy_ (u"ࠨࡁ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠥᄲ"),
                                bstack11l1l11_opy_ (u"ࠢࡥࡣࡷࡥࠧᄳ"): data,
                                bstack11l1l11_opy_ (u"ࠣ࡮ࡨࡺࡪࡲࠢᄴ"): bstack11l1l11_opy_ (u"ࠤࡧࡩࡧࡻࡧࠣᄵ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦ࡯࠲࠳ࡼࠤࡦࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡾࢁࠧᄶ"), e)
    def bstack1lll1l11lll_opy_(
        self,
        instance: bstack1lll1l1ll11_opy_,
        f: TestFramework,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1llll_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1ll11ll_opy_.bstack1llll111111_opy_, False):
            return
        self.bstack1llllllll11_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1ll111_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l1l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l1111l_opy_)
        req.test_framework_state = bstack11111111l1_opy_[0].name
        req.test_hook_state = bstack11111111l1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll11l1ll_opy_)
        for bstack1lll1lll1l1_opy_ in bstack1lll1ll11l1_opy_.bstack1lll1lll111_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack11l1l11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠥᄷ")
                if bstack1llll11llll_opy_
                else bstack11l1l11_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࡥࡧࡳ࡫ࡧࠦᄸ")
            )
            session.ref = bstack1lll1lll1l1_opy_.ref()
            session.hub_url = bstack1lll1ll11l1_opy_.get_state(bstack1lll1lll1l1_opy_, bstack1lll1ll11l1_opy_.bstack1lll1l1l11l_opy_, bstack11l1l11_opy_ (u"ࠨࠢᄹ"))
            session.framework_name = bstack1lll1lll1l1_opy_.framework_name
            session.framework_version = bstack1lll1lll1l1_opy_.framework_version
            session.framework_session_id = bstack1lll1ll11l1_opy_.get_state(bstack1lll1lll1l1_opy_, bstack1lll1ll11l1_opy_.bstack1lll1l11ll1_opy_, bstack11l1l11_opy_ (u"ࠢࠣᄺ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1llll111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs
    ):
        bstack1llll11ll1l_opy_ = f.get_state(instance, bstack1lll1ll11ll_opy_.bstack1llll11l11l_opy_, [])
        if not bstack1llll11ll1l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄻ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠤࠥᄼ"))
            return
        if len(bstack1llll11ll1l_opy_) > 1:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄽ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠦࠧᄾ"))
        bstack1llll1l11l1_opy_, bstack1lll1l11l11_opy_ = bstack1llll11ll1l_opy_[0]
        page = bstack1llll1l11l1_opy_()
        if not page:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄿ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠨࠢᅀ"))
            return
        return page
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll11ll11_opy_ = {}
        for bstack1lll1lll1l1_opy_ in bstack1lll1ll11l1_opy_.bstack1lll1lll111_opy_.values():
            caps = bstack1lll1ll11l1_opy_.get_state(bstack1lll1lll1l1_opy_, bstack1lll1ll11l1_opy_.bstack1lll1ll1l1l_opy_, bstack11l1l11_opy_ (u"ࠢࠣᅁ"))
        bstack1llll11ll11_opy_[bstack11l1l11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨᅂ")] = caps.get(bstack11l1l11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥᅃ"), bstack11l1l11_opy_ (u"ࠥࠦᅄ"))
        bstack1llll11ll11_opy_[bstack11l1l11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥᅅ")] = caps.get(bstack11l1l11_opy_ (u"ࠧࡵࡳࠣᅆ"), bstack11l1l11_opy_ (u"ࠨࠢᅇ"))
        bstack1llll11ll11_opy_[bstack11l1l11_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᅈ")] = caps.get(bstack11l1l11_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧᅉ"), bstack11l1l11_opy_ (u"ࠤࠥᅊ"))
        bstack1llll11ll11_opy_[bstack11l1l11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦᅋ")] = caps.get(bstack11l1l11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨᅌ"), bstack11l1l11_opy_ (u"ࠧࠨᅍ"))
        return bstack1llll11ll11_opy_
    def bstack1lll1l1l1l1_opy_(self, page: object, bstack1lll1llll11_opy_, args={}):
        try:
            bstack1lll1l1ll1l_opy_ = bstack11l1l11_opy_ (u"ࠨࠢࠣࠪࡩࡹࡳࡩࡴࡪࡱࡱࠤ࠭࠴࠮࠯ࡤࡶࡸࡦࡩ࡫ࡔࡦ࡮ࡅࡷ࡭ࡳࠪࠢࡾࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡷࡹࡷࡴࠠ࡯ࡧࡺࠤࡕࡸ࡯࡮࡫ࡶࡩ࠭࠮ࡲࡦࡵࡲࡰࡻ࡫ࠬࠡࡴࡨ࡮ࡪࡩࡴࠪࠢࡀࡂࠥࢁࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡵࡷࡥࡨࡱࡓࡥ࡭ࡄࡶ࡬ࡹ࠮ࡱࡷࡶ࡬࠭ࡸࡥࡴࡱ࡯ࡺࡪ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡼࡨࡱࡣࡧࡵࡤࡺࡿࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࡽࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࢀ࠭࠭ࢁࡡࡳࡩࡢ࡮ࡸࡵ࡮ࡾࠫࠥࠦࠧᅎ")
            bstack1lll1llll11_opy_ = bstack1lll1llll11_opy_.replace(bstack11l1l11_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᅏ"), bstack11l1l11_opy_ (u"ࠣࡤࡶࡸࡦࡩ࡫ࡔࡦ࡮ࡅࡷ࡭ࡳࠣᅐ"))
            script = bstack1lll1l1ll1l_opy_.format(fn_body=bstack1lll1llll11_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠤࡤ࠵࠶ࡿ࡟ࡴࡥࡵ࡭ࡵࡺ࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡈࡶࡷࡵࡲࠡࡧࡻࡩࡨࡻࡴࡪࡰࡪࠤࡹ࡮ࡥࠡࡣ࠴࠵ࡾࠦࡳࡤࡴ࡬ࡴࡹ࠲ࠠࠣᅑ") + str(e) + bstack11l1l11_opy_ (u"ࠥࠦᅒ"))