# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l111111_opy_, bstack11l11lll11l_opy_, bstack11l1l11l11l_opy_
import tempfile
import json
bstack11111lllll1_opy_ = os.getenv(bstack1ll1ll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡉࡢࡊࡎࡒࡅࠣầ"), None) or os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡥࡧࡥࡹ࡬࠴࡬ࡰࡩࠥẨ"))
bstack11111l1llll_opy_ = os.path.join(bstack1ll1ll1_opy_ (u"ࠤ࡯ࡳ࡬ࠨẩ"), bstack1ll1ll1_opy_ (u"ࠪࡷࡩࡱ࠭ࡤ࡮࡬࠱ࡩ࡫ࡢࡶࡩ࠱ࡰࡴ࡭ࠧẪ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1ll1ll1_opy_ (u"ࠫࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧẫ"),
      datefmt=bstack1ll1ll1_opy_ (u"࡙ࠬࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࡜ࠪẬ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l1l1111l_opy_():
  bstack11111lll111_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡊࡅࡃࡗࡊࠦậ"), bstack1ll1ll1_opy_ (u"ࠢࡧࡣ࡯ࡷࡪࠨẮ"))
  return logging.DEBUG if bstack11111lll111_opy_.lower() == bstack1ll1ll1_opy_ (u"ࠣࡶࡵࡹࡪࠨắ") else logging.INFO
def bstack1ll11ll1ll1_opy_():
  global bstack11111lllll1_opy_
  if os.path.exists(bstack11111lllll1_opy_):
    os.remove(bstack11111lllll1_opy_)
  if os.path.exists(bstack11111l1llll_opy_):
    os.remove(bstack11111l1llll_opy_)
def bstack1111lllll1_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack1111l1111ll_opy_ = log_level
  if bstack1ll1ll1_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫẰ") in config and config[bstack1ll1ll1_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬằ")] in bstack11l11lll11l_opy_:
    bstack1111l1111ll_opy_ = bstack11l11lll11l_opy_[config[bstack1ll1ll1_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭Ẳ")]]
  if config.get(bstack1ll1ll1_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧẳ"), False):
    logging.getLogger().setLevel(bstack1111l1111ll_opy_)
    return bstack1111l1111ll_opy_
  global bstack11111lllll1_opy_
  bstack1111lllll1_opy_()
  bstack11111l1ll11_opy_ = logging.Formatter(
    fmt=bstack1ll1ll1_opy_ (u"࠭ࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩẴ"),
    datefmt=bstack1ll1ll1_opy_ (u"࡛ࠧࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࡞ࠬẵ"),
  )
  bstack11111ll11ll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111lllll1_opy_)
  file_handler.setFormatter(bstack11111l1ll11_opy_)
  bstack11111ll11ll_opy_.setFormatter(bstack11111l1ll11_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111ll11ll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1ll1ll1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷ࠴ࡲࡦ࡯ࡲࡸࡪ࠴ࡲࡦ࡯ࡲࡸࡪࡥࡣࡰࡰࡱࡩࡨࡺࡩࡰࡰࠪẶ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111ll11ll_opy_.setLevel(bstack1111l1111ll_opy_)
  logging.getLogger().addHandler(bstack11111ll11ll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack1111l1111ll_opy_
def bstack11111ll111l_opy_(config):
  try:
    bstack11111llll1l_opy_ = set(bstack11l1l11l11l_opy_)
    bstack1111l11111l_opy_ = bstack1ll1ll1_opy_ (u"ࠩࠪặ")
    with open(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭Ẹ")) as bstack11111lll11l_opy_:
      bstack1111l1111l1_opy_ = bstack11111lll11l_opy_.read()
      bstack1111l11111l_opy_ = re.sub(bstack1ll1ll1_opy_ (u"ࡶࠬࡤࠨ࡝ࡵ࠮࠭ࡄࠩ࠮ࠫࠦ࡟ࡲࠬẹ"), bstack1ll1ll1_opy_ (u"ࠬ࠭Ẻ"), bstack1111l1111l1_opy_, flags=re.M)
      bstack1111l11111l_opy_ = re.sub(
        bstack1ll1ll1_opy_ (u"ࡸࠧ࡟ࠪ࡟ࡷ࠰࠯࠿ࠩࠩẻ") + bstack1ll1ll1_opy_ (u"ࠧࡽࠩẼ").join(bstack11111llll1l_opy_) + bstack1ll1ll1_opy_ (u"ࠨࠫ࠱࠮ࠩ࠭ẽ"),
        bstack1ll1ll1_opy_ (u"ࡴࠪࡠ࠷ࡀࠠ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫẾ"),
        bstack1111l11111l_opy_, flags=re.M | re.I
      )
    def bstack11111lll1l1_opy_(dic):
      bstack11111ll1lll_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111llll1l_opy_:
          bstack11111ll1lll_opy_[key] = bstack1ll1ll1_opy_ (u"ࠪ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧế")
        else:
          if isinstance(value, dict):
            bstack11111ll1lll_opy_[key] = bstack11111lll1l1_opy_(value)
          else:
            bstack11111ll1lll_opy_[key] = value
      return bstack11111ll1lll_opy_
    bstack11111ll1lll_opy_ = bstack11111lll1l1_opy_(config)
    return {
      bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧỀ"): bstack1111l11111l_opy_,
      bstack1ll1ll1_opy_ (u"ࠬ࡬ࡩ࡯ࡣ࡯ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨề"): json.dumps(bstack11111ll1lll_opy_)
    }
  except Exception as e:
    return {}
def bstack11111lll1ll_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1ll1ll1_opy_ (u"࠭࡬ࡰࡩࠪỂ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111l1lll1_opy_ = os.path.join(log_dir, bstack1ll1ll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡤࡱࡱࡪ࡮࡭ࡳࠨể"))
  if not os.path.exists(bstack11111l1lll1_opy_):
    bstack11111ll1l1l_opy_ = {
      bstack1ll1ll1_opy_ (u"ࠣ࡫ࡱ࡭ࡵࡧࡴࡩࠤỄ"): str(inipath),
      bstack1ll1ll1_opy_ (u"ࠤࡵࡳࡴࡺࡰࡢࡶ࡫ࠦễ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1ll1ll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩỆ")), bstack1ll1ll1_opy_ (u"ࠫࡼ࠭ệ")) as bstack11111llll11_opy_:
      bstack11111llll11_opy_.write(json.dumps(bstack11111ll1l1l_opy_))
def bstack1111l111111_opy_():
  try:
    bstack11111l1lll1_opy_ = os.path.join(os.getcwd(), bstack1ll1ll1_opy_ (u"ࠬࡲ࡯ࡨࠩỈ"), bstack1ll1ll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹ࠮࡫ࡵࡲࡲࠬỉ"))
    if os.path.exists(bstack11111l1lll1_opy_):
      with open(bstack11111l1lll1_opy_, bstack1ll1ll1_opy_ (u"ࠧࡳࠩỊ")) as bstack11111llll11_opy_:
        bstack11111ll1ll1_opy_ = json.load(bstack11111llll11_opy_)
      return bstack11111ll1ll1_opy_.get(bstack1ll1ll1_opy_ (u"ࠨ࡫ࡱ࡭ࡵࡧࡴࡩࠩị"), bstack1ll1ll1_opy_ (u"ࠩࠪỌ")), bstack11111ll1ll1_opy_.get(bstack1ll1ll1_opy_ (u"ࠪࡶࡴࡵࡴࡱࡣࡷ࡬ࠬọ"), bstack1ll1ll1_opy_ (u"ࠫࠬỎ"))
  except:
    pass
  return None, None
def bstack11111l1ll1l_opy_():
  try:
    bstack11111l1lll1_opy_ = os.path.join(os.getcwd(), bstack1ll1ll1_opy_ (u"ࠬࡲ࡯ࡨࠩỏ"), bstack1ll1ll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹ࠮࡫ࡵࡲࡲࠬỐ"))
    if os.path.exists(bstack11111l1lll1_opy_):
      os.remove(bstack11111l1lll1_opy_)
  except:
    pass
def bstack1l1l1l1l_opy_(config):
  try:
    from bstack_utils.helper import bstack11111l11_opy_, bstack11l1l1l11_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111lllll1_opy_
    if config.get(bstack1ll1ll1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩố"), False):
      return
    uuid = os.getenv(bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭Ồ")) if os.getenv(bstack1ll1ll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧồ")) else bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧỔ"))
    if not uuid or uuid == bstack1ll1ll1_opy_ (u"ࠫࡳࡻ࡬࡭ࠩổ"):
      return
    bstack11111ll11l1_opy_ = [bstack1ll1ll1_opy_ (u"ࠬࡸࡥࡲࡷ࡬ࡶࡪࡳࡥ࡯ࡶࡶ࠲ࡹࡾࡴࠨỖ"), bstack1ll1ll1_opy_ (u"࠭ࡐࡪࡲࡩ࡭ࡱ࡫ࠧỗ"), bstack1ll1ll1_opy_ (u"ࠧࡱࡻࡳࡶࡴࡰࡥࡤࡶ࠱ࡸࡴࡳ࡬ࠨỘ"), bstack11111lllll1_opy_, bstack11111l1llll_opy_]
    bstack11111ll1l11_opy_, root_path = bstack1111l111111_opy_()
    if bstack11111ll1l11_opy_ != None:
      bstack11111ll11l1_opy_.append(bstack11111ll1l11_opy_)
    if root_path != None:
      bstack11111ll11l1_opy_.append(os.path.join(root_path, bstack1ll1ll1_opy_ (u"ࠨࡥࡲࡲ࡫ࡺࡥࡴࡶ࠱ࡴࡾ࠭ộ")))
    bstack1111lllll1_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯࡯ࡳ࡬ࡹ࠭ࠨỚ") + uuid + bstack1ll1ll1_opy_ (u"ࠪ࠲ࡹࡧࡲ࠯ࡩࡽࠫớ"))
    with tarfile.open(output_file, bstack1ll1ll1_opy_ (u"ࠦࡼࡀࡧࡻࠤỜ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111ll11l1_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111ll111l_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111ll1111_opy_ = data.encode()
        tarinfo.size = len(bstack11111ll1111_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111ll1111_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack1ll1ll1_opy_ (u"ࠬࡪࡡࡵࡣࠪờ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1ll1ll1_opy_ (u"࠭ࡲࡣࠩỞ")), bstack1ll1ll1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡾ࠭ࡨࡼ࡬ࡴࠬở")),
        bstack1ll1ll1_opy_ (u"ࠨࡥ࡯࡭ࡪࡴࡴࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪỠ"): uuid
      }
    )
    bstack11111llllll_opy_ = bstack11l1l1l11_opy_(cli.config, [bstack1ll1ll1_opy_ (u"ࠤࡤࡴ࡮ࡹࠢỡ"), bstack1ll1ll1_opy_ (u"ࠥࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠥỢ"), bstack1ll1ll1_opy_ (u"ࠦࡺࡶ࡬ࡰࡣࡧࠦợ")], bstack11l1l111111_opy_)
    response = requests.post(
      bstack1ll1ll1_opy_ (u"ࠧࢁࡽ࠰ࡥ࡯࡭ࡪࡴࡴ࠮࡮ࡲ࡫ࡸ࠵ࡵࡱ࡮ࡲࡥࡩࠨỤ").format(bstack11111llllll_opy_),
      data=multipart_data,
      headers={bstack1ll1ll1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬụ"): multipart_data.content_type},
      auth=(config[bstack1ll1ll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩỦ")], config[bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫủ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1ll1ll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡷࡳࡰࡴࡧࡤࠡ࡮ࡲ࡫ࡸࡀࠠࠨỨ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1ll1ll1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡰࡴ࡭ࡳ࠻ࠩứ") + str(e))
  finally:
    try:
      bstack1ll11ll1ll1_opy_()
      bstack11111l1ll1l_opy_()
    except:
      pass